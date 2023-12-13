import requests
import os
import pandas as pd
import json
from bs4 import BeautifulSoup
from libs import excelExport

def ultratiming(url):
    df = get_all_pages_results(url, pd.DataFrame())

    # Move sub columns to columns
    df['userFirstName'] = df['user'].apply(lambda x: x['firstName'])
    df['userLastName'] = df['user'].apply(lambda x: x['lastName'])
    df['userNationality'] = df['user'].apply(lambda x: x['nationality'])
    df['userBirthDate'] = df['user'].apply(lambda x: x['birthDate'])

    # remove rows with rank nan
    df = df[df['rank'].notna()]

    # Keep columns userFirstName, userLastName, userNationality, userBirthDate, finalTime, club, category, raceNumber, gender
    df = df[['userFirstName', 'userLastName', 'userNationality', 'userBirthDate', 'finalTime', 'club', 'category', 'raceNumber', 'gender']]

    # Change userBirthDate format from 1990-01-01T00:00:00+01:00 to 1990
    df['userBirthDate'] = df['userBirthDate'].str.split('-').str[0]

    return [excelExport.excel_export(df, "ultratiming")]



def get_all_pages_results(url, dataframe):
    pageurlttr = '?page='
    if dataframe.shape[0] % 100 == 0:
        # Get the html page
        html = requests.get(url)
        if url.split(pageurlttr).__len__() == 1:
            page = 1
        else:
            page = int(url.split(pageurlttr)[1])
        # Parse the html page with BeautifulSoup
        soup = BeautifulSoup(html.content, 'html.parser')
        # Get the data included in the script with id "__NEXT_DATA__"
        scriptcontent = soup.find(id="__NEXT_DATA__").text
        # Convert the scriptContent (json string) to a python dictionary
        scriptcontentobj = json.loads(scriptcontent)
        # print(scriptcontentobj['props']['pageProps']['resultsResult'])
        df = pd.DataFrame(scriptcontentobj['props']['pageProps']['resultsResult']['hydra:member'])
        # append df to dataframe
        dataframe = dataframe.append(df, ignore_index=True)
        return get_all_pages_results(url.split(pageurlttr)[0] + pageurlttr + str(page + 1), dataframe)
    return dataframe
    

