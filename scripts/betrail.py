import requests
import pandas as pd
import datetime

def betrail_backyard(url, year, str_to_contain):
    requests.get(url)

    #Parse the main JSON
    data = requests.get(url).json()
    all_events = data["body"]["events"]

    event = [event for event in all_events if (datetime.datetime.fromtimestamp(event["date"]).strftime('%Y').startswith(str(year)))][0]

    all_distances = event["races"]
    if str_to_contain != "":
        all_distances = [distance for distance in all_distances if str_to_contain in distance["title"]]
    all_race_df = pd.DataFrame(all_distances, columns=["id", "distance", "elevation", "betrail_index"])

    all_race_results = []
    #Get each race results
    for idx, race in all_race_df.iterrows():
        race_url = "https://www.betrail.run/api/encodage/race/" + str(race['id']) + "/results"
        race_raw_result = requests.get(race_url).json()
        race_result = race_raw_result["body"]
        race_result_df = pd.DataFrame(race_result)
        race_result_df = race_result_df.loc[:, ['performance', 'position', 'points', 'result_seconds']]  # Select only specific columns
        all_race_results.append(race_result_df)  # Append race result to the list

    all_race_df['results'] = all_race_results  # Add results column to all_race_df
    
    return all_race_df

def betrail_backyard_getperformance(url, year, lap_length, string_to_contain=""):
    all_distances_df = betrail_backyard(url, year, string_to_contain)
    performances = []
    for idx, distance in all_distances_df.iterrows():
        lap_count=round(distance['distance']/lap_length,0)
        mean_performance=0
        performances_list = distance['results']['performance']
        finisher_count = len(performances_list)
        mean_performance = sum(performances_list)/finisher_count
        median_performance = sorted(performances_list)[finisher_count//2]
        performances.append([lap_count, distance["distance"], finisher_count, median_performance, mean_performance, distance['betrail_index']])
    columns = ["lap_count", "distance", "runner_count", "worst_prono", "average_prono", "old_index"]
    performances_df = pd.DataFrame(performances, columns=columns)
    return performances_df