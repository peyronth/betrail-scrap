import pandas as pd
import libs.excelExport as excelExport
from bs4 import BeautifulSoup
import tkinter as tk

def raceresult(html): 
    #Parse html
    soup = BeautifulSoup(html, 'html.parser')

    #Get table with class MainTable
    table = soup.find("table", {"class": "MainTable"})
    
    # Table to panda dataframe
    df = pd.read_html(str(table))[0]
    
    # Ask for the name of the time column
    root = tk.Tk()
    root.withdraw()
    time_column_name = ""
    while time_column_name == "" or time_column_name not in df.columns:
        time_column_name = tk.simpledialog.askstring("Time column name", "What is the name of the time column?")

    # Remove row with Time NaN
    df = df.dropna(subset=[time_column_name])

    # Split Name to Firstname and Lastname with ","
    if 'Name' in df.columns and ',' in df['Name'].iloc[1]:
        df[['Firstname','Lastname']] = df['Name'].str.split(',',expand=True)

    return [excelExport.excel_export(df, "raceresult")]




