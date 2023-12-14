import requests
import pandas as pd
import json
from libs import excelExport

def utmbworld(url):
    # Convert https://kosciuszko.utmb.world/runners/results?year=2023&raceUri=33948.ultra-trailkosciuszkobyutmbkoscimiler.2023 to https://api.utmb.world/races/33948.ultra-trailkosciuszkobyutmbkoscimiler.2023/results
    urlsplit = url.split("/")
    raceuri = urlsplit[4].split("&")[1].split("=")[1]
    apiurl = "https://api.utmb.world/races/" + raceuri + "/results?lang=en&offset=0&limit=1000000"

    # Get the data
    response = requests.get(apiurl)
    
    # Read JSON and get results
    data = response.json()
    results = data["results"]
    
    # Create a dataframe
    df = pd.DataFrame(results)
    
    # Remove columns runnerUri, index
    df = df.drop(columns=["runnerUri", "index"])

    # Column gender replace H by M
    df["gender"] = df["gender"].replace("H", "M")
    
    # Drop row where time is None
    df = df.dropna(subset=["time"])

    return [excelExport.excel_export(df, "utmbworld")]
