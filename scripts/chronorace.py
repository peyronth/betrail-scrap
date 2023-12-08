import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os
from libs import excelExport

def chronorace(file_url):
    file = requests.get(file_url)
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
    country_file_path = './ressources/country.csv'
    country = pd.read_csv(country_file_path, sep=',')
    country = country.set_index('alpha-3')
    df[7] = df[7].replace(country['alpha-2'].to_dict())
    # Remove row with column 9 to Nan
    df = df.dropna(subset=[9])
    # Remove row with column 1 to "DSQ"
    df = df[df[1] != 'DSQ']
    # Remove column 0, 3, 4, 6, 11, 12
    df = df.drop(columns=[0, 3, 4, 6, 11, 12])
    # Export to excel, file name is the timestamp
    return excelExport.excel_export(df, "chronorace")