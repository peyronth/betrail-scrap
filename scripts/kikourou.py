# import
import requests
import os
from libs import excelExport

def kikourou(fileurl):
    file = requests.get(fileurl)
    # Parse the file
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(file.content, 'html.parser')
    # Get the table
    table = soup.find('table', attrs={'id': 'results'})
    # Parse the table to get the data
    import pandas as pd
    df = pd.read_html(str(table))[0]
    # Convert column Perf (format %Hh%M'%S'') to seconds
    import datetime
    df['Perf'] = df['Perf'].apply(lambda x: datetime.datetime.strptime(x, '%Hh%M\'%S\'\'').time())
    # Create column gender with the last letter of the column Cat
    df['Gender'] = df['Cat'].str[-1]
    # Remove Cat column
    df = df.drop(columns=['Cat'])
    return [excelExport.excel_export(df, "kikourou")]
