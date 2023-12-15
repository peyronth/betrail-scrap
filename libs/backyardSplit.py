import pandas as pd
from libs import excelExport

def exportbybistance(df, distancecolumn): 
    # Sort each sub dataset by time in ascending order
    sub_datasets = df.groupby(distancecolumn)

    filesnames = []
    # Export each sorted sub dataset to Excel
    for race, sub_dataset in sub_datasets:
        distance = sub_dataset[distancecolumn].iloc[0]
        filesnames.append(excelExport.excel_export(sub_dataset, "--backyard--" + str(distance) + "--"))

    return filesnames

def excelsplitdistance(filepath, distancecolumn = "Distance"):
    # Create pandas dataframe from excel file
    df = pd.read_excel(filepath)
    return exportbybistance(df, distancecolumn)

