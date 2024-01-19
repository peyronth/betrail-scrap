import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def interpolate_selected_perf(performances_df):
    performances_df['selected_prono'] = performances_df[['worst_prono', 'average_prono']].min(axis=1)
    train_df = performances_df.dropna(subset=['average_prono']).copy()

    # Linear interpolation of selected_prono by lap_count
    slope, intercept = np.polyfit(train_df['lap_count'], train_df['selected_prono'], 1)
    print(f"Equation de la droite : y = {slope}x + {intercept}")
    
    # Power interpolation of selected_prono by lap_count (y = ax^b)
    n = len(train_df['lap_count'])
    sum_lap_count, sum_lap_count2, sum_selected_prono, sum_xy = 0, 0, 0, 0
    for index, distance in train_df.iterrows():
        sum_lap_count = sum_lap_count + np.log(distance['lap_count'])
        sum_lap_count2 = sum_lap_count2 + np.log(distance['lap_count']) * np.log(distance['lap_count'])
        sum_selected_prono = sum_selected_prono + np.log(distance['selected_prono'])
        sum_xy = sum_xy + np.log(distance['lap_count']) * np.log(distance['selected_prono'])

    # Finding coefficients A and B
    b = (n * sum_xy - sum_lap_count * sum_selected_prono) / (n * sum_lap_count2 - sum_lap_count * sum_lap_count)
    a = np.exp((sum_selected_prono - b * sum_lap_count) / n)

    # For each lap_count add column with the min between linear and power interpolation
    performances_df['linear_interpolation'] = performances_df['lap_count'].apply(lambda x: slope*x + intercept)
    performances_df['power_interpolation'] = performances_df['lap_count'].apply(lambda x: a*x**b)
    performances_df['interpolation'] = performances_df[['linear_interpolation', 'power_interpolation']].min(axis=1)
    return performances_df

def compute_index(interpolated_df):
    constant = 0.864
    # Compute index
    interpolated_df['index'] = round(interpolated_df['lap_count'] * interpolated_df['interpolation'] * 3600/100/constant, 0)
    return interpolated_df

performances = [
    [1, 2, 35.01, 43.81],
    [2, 6, 41.99, 36.81],
    [3, 16, 42.50, 43.33],
    [4, 23, 44.82, 42.90],
    [5, 34, 44.28, 45.46],
    [6, 38, 46.63, 47.57],
    [7, 25, 47.59, 48.92],
    [8, 28, 48.55, 50.88],
    [9, 17, 49.71, 51.36],
    [10, 29, 50.82, 51.09],
    [11, 12, 54.50, 53.31],
    [12, 11, 56.51, 55.22],
    [13, None, None, None],
    [14, None, None, None],
    [15, 3, 62.82, 60.46],
    [17, 5, 61.41, 61.41],
    [18, 1, 56.49, 56.49],
    [19, 3, 65.00, 65.02],
    [24, 4, 70.64, 69.43],
    [30, None, None, None],
    [40, None, None, None],
    [50, None, None, None],
    [60, None, None, None],
    [85, None, None, None]
]

columns = ["lap_count", "runner_count", "worst_prono", "average_prono"]
performances_df = pd.DataFrame(performances, columns=columns)
