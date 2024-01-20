import pandas as pd
import libs.excelExport as excelExport
from bs4 import BeautifulSoup
import tkinter as tk
import libs.classes.SimpleChoiceBox as SimpleChoiceBox

def raceresult(html): 
    #Parse html
    soup = BeautifulSoup(html, 'html.parser')

    #Get table with class MainTable
    table = soup.find("table", {"class": "MainTable"})

    # Remove all <tr> with class "withDetails"
    for tr in table.find_all("tr", {"class": "withDetails"}):
        tr.decompose()
    
    # Remove all <tr> with class "brokeColsButtons"
    for tr in table.find_all("tr", {"class": "brokeColsButtons"}):
        tr.decompose()
    
    # Table to panda dataframe
    df = pd.read_html(str(table))[0]
    
    # Ask for the name of the time column
    root = tk.Tk()
    root.withdraw()
    time_column_name = (SimpleChoiceBox.SimpleChoiceBox("Time column name", "What is the name of the time column?", df.columns.values)).selection
    name_column_name = ""
    while name_column_name == "" or name_column_name not in df.columns:
        name_column_name = tk.simpledialog.askstring("Name column name", "What is the name of the name column? (If not fullname column to split enter \"Null\")")

    # Remove row with Time NaN
    df = df.dropna(subset=[time_column_name])

    # Split Name to Firstname and Lastname with ","
    if name_column_name in df.columns and ',' in df[name_column_name].iloc[1]:
        df[['Firstname','Lastname']] = df[name_column_name].str.split(',',expand=True)

    return [excelExport.excel_export(df, "raceresult")]




