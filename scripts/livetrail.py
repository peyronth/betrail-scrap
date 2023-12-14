import requests
import pandas as pd
from bs4 import BeautifulSoup
from libs import excelExport

def livetrail(url):
    # Get the html content
    xml = requests.get(url).content

    # Parse the xml and get <classement> tag
    soup = BeautifulSoup(xml, 'xml')
    classement = soup.find('classement')
    
    # Get all <c> inside <classement>
    c = classement.find_all('c')

    # Build panda dataframe from <c> attributes
    df = pd.DataFrame()
    for i in range(len(c)):
        df = df.append(c[i].attrs, ignore_index=True)

    # Remove column pays, cio, ph, index, ecart
    df = df.drop(columns=['pays', 'cio', 'ph', 'index', 'ecart'])

    return [excelExport.excel_export(df, "--livetrail--")]

livetrail("https://livetrail.net/histo/kosciuszko_2023/classement.php?course=100k&cat=scratch")