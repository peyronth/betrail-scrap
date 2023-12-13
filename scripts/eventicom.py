import requests
import pandas as pd
from bs4 import BeautifulSoup
from libs import excelExport


def eventicom(url):
    xmlraw = requests.get(url)

    # xmlRaw is an xml data file. We need to parse it to get the data we want
    soup = BeautifulSoup(xmlraw.content, 'xml')
    runner = soup.Epreuve.Etapes.Etape.Engages.find_all('E')
    results = soup.Epreuve.Etapes.Etape.Resultats.find_all('R')


    # Runner is a list of html tags (E) containing the data we want as attributes. We need to parse it to get the data we want in a pandas dataframe
    df_runner = pd.DataFrame()
    for i in range(len(runner)):
        df_runner = df_runner.append(runner[i].attrs, ignore_index=True)
    df_results = pd.DataFrame()
    for i in range(len(results)):
        df_results = df_results.append(results[i].attrs, ignore_index=True)

    # Join each runner with his result (runner.d = result.d)
    df = df_runner.merge(df_results, on='d')

    # just keep columns n, a, x, ca, c, p, na, re
    df = df[['n', 'a', 'x', 'ca', 'c', 'p', 'na', 're']]
    df = df.rename(columns={'n': 'name', 'a': 'year', 'x': 'gender', 'ca': 'category', 'c': 'club', 'p': 'race', 'na': 'country', 're': 'time'})

    # Replace column 7 (3 digit country code) by 2 digit country code
    country_file_path = './ressources/country.csv'
    country = pd.read_csv(country_file_path, sep=',')
    country = country.set_index('alpha-3')
    df['country'] = df['country'].replace(country['alpha-2'].to_dict())

    # convert time from %Hh%M'%S to %H:%M:%S
    df['time'] = df['time'].str.replace('h', ':').str.replace("'", ':')

    # Remove rows with no time or time Nan
    df = df[df['time'] != '']
    df = df[df['time'].notna()]

    # Split dataset to sub dataset by race
    sub_datasets = df.groupby('race')

    # Sort each sub dataset by time in ascending order
    sorted_sub_datasets = {race: sub_dataset.sort_values('time') for race, sub_dataset in sub_datasets}

    filesnames = []
    # Export each sorted sub dataset to Excel
    for race, sorted_sub_dataset in sorted_sub_datasets.items():
        filesnames.append(excelExport.excel_export(sorted_sub_dataset, "--" + race + "--eventicom"))

    return filesnames
