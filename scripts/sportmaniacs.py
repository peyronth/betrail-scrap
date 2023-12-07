import json
import requests
import pandas as pd
import datetime
import os
from bs4 import BeautifulSoup
from libs import excelExport


def sportmaniacs(ranking_url):
    race_country = ranking_url.split("/")[3]
    race_id = ranking_url.split("/")[6]
    true_url = "https://sportmaniacs.com/" + race_country + "/races/rankings/" + race_id 
    results_json = requests.get(true_url).content
    #Json decode to and select the data
    results_json = json.loads(results_json)
    results_data = results_json['data']
    #Create a dataframe with the data resultsData['Rankings'] (type list)
    df = pd.DataFrame(results_data['Rankings'])
    #Select the columns dorsal, name, club, nationality, gender, category, realPos, realTime
    df = df[["dorsal", "name", "club", "nationality", "gender", "category", "realPos", "realTime"]]
    # Remove row if realTime is 00:00:00 or if realPos is NaN
    df = df[df['realTime'] != "00:00:00"]
    df = df.dropna(subset=['realPos'])
    df = df[df['realPos'] != ""]
    # In gender replace gender_0 by M and gender_1 by F
    df['gender'] = df['gender'].replace({'gender_0': 'M', 'gender_1': 'F'})
    # Excel export
    return excelExport.excel_export(df, "sportmaniacs")
