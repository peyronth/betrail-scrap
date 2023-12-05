import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os

fileUrl = "https://prod.chronorace.be/Classements/Classement.aspx?eventId=1188318666566175&IdClassement=17573"

file = requests.get(fileUrl)

# Get all tr with class "Even" or "Odd"
soup = BeautifulSoup(file.content, 'html.parser')
table = soup.find_all('tr', attrs={'class': ['Even', 'Odd']})

# add <table> and </table> tags and remove [ and ] in table
table = str(table).replace('[', '').replace(']', '').replace('\'', '')
table = '<table>' + str(table) + '</table>'

# Table to panda
df = pd.read_html(table)[0]

# Create column gender with the last letter of the column Cat replacing h by M and f by F
df['Gender'] = df[14].str[-1].replace('h', 'M').replace('f', 'F')
# Column Gender replace "x" by "M"
df['Gender'] = df['Gender'].replace('x', 'M')

# Replace column 7 (3 digit country code) by 2 digit country code
countryFilePath = './ressources/country.csv'
country = pd.read_csv(countryFilePath, sep=',')
country = country.set_index('alpha-3')
df[7] = df[7].replace(country['alpha-2'].to_dict())

# Remove row with column 9 to Nan
df = df.dropna(subset=[9])

# Remove row with column 1 to "DSQ"
df = df[df[1] != 'DSQ']

# Remove column 0, 3, 4, 6, 11, 12
df = df.drop(columns=[0, 3, 4, 6, 11, 12])

# Export to excel, file name is the timestamp
excelFileName = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".xlsx"
exportFolderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "export")
excelFilePath = os.path.join(exportFolderPath, excelFileName)
df.to_excel(excelFilePath, index=False, header=False)