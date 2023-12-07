import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os

rankingUrl = "https://sportmaniacs.com/es/races/gtpe-2023-gran-trail-picos-de-europa/6496d988-abcc-48c1-ab80-2eaeac1f1c02/results#rankings"

raceCountry = rankingUrl.split("/")[3]
raceId = rankingUrl.split("/")[6]
trueUrl = "https://sportmaniacs.com/" + raceCountry + "/races/rankings/" + raceId 

resultsJson = requests.get(trueUrl).content

#Json decode to and select the data
resultsJson = json.loads(resultsJson)
resultsData = resultsJson['data']

#Create a dataframe with the data resultsData['Rankings'] (type list)
df = pd.DataFrame(resultsData['Rankings'])

#Select the columns dorsal, name, club, nationality, gender, category, realPos, realTime
df = df[["dorsal", "name", "club", "nationality", "gender", "category", "realPos", "realTime"]]


# Remove row if realTime is 00:00:00 or if realPos is NaN
df = df[df['realTime'] != "00:00:00"]
df = df.dropna(subset=['realPos'])
df = df[df['realPos'] != ""]

# In gender replace gender_0 by M and gender_1 by F
df['gender'] = df['gender'].replace({'gender_0': 'M', 'gender_1': 'F'})

#Export to excel, file name is the timestamp
excelFileName = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".xlsx"
exportFolderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "export")
excelFilePath = os.path.join(exportFolderPath, excelFileName)
df.to_excel(excelFilePath, index=False, header=False)