import pandas as pd
import libs.excelExport as excelExport
from bs4 import BeautifulSoup

def raceresult(html): 
    #Parse html
    soup = BeautifulSoup(html, 'html.parser')

    #Get table with class MainTable
    table = soup.find("table", {"class": "MainTable"})
    
    # Table to panda dataframe
    df = pd.read_html(str(table))[0]
    
    #Keep columns Bib, Name, Gender, Nat., YoB, Club, Time
    df = df[["Bib", "Name", "Gender", "Nat.", "YoB", "Club", "Time"]]

    # Remove row with Time NaN
    df = df.dropna(subset=['Time'])

    # Split Name to Firstname and Lastname with ","
    df[['Firstname','Lastname']] = df['Name'].str.split(',',expand=True)

    return [excelExport.excel_export(df, "raceresult")]




