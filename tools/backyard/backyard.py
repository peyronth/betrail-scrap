import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def interpolate_selected_perf(performances_df):
    performances_df['selected_prono'] = performances_df[['worst_prono', 'average_prono']].min(axis=1)
    train_df = performances_df.dropna(subset=['average_prono']).copy()

    # Linear interpolation of selected_prono by lap_count
    slope, intercept = np.polyfit(train_df['lap_count'], train_df['selected_prono'], 1)
    
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

    print(f"Equation de la droite : y = {slope}x + {intercept}")
    print(f"Equation de la courbe : y = {a}x^{b}")

    return performances_df

def compute_index(interpolated_df):
    constant = 0.864
    # Compute index
    interpolated_df['index'] = round(interpolated_df['lap_count'] * interpolated_df['interpolation'] * 3600/100/constant, 0)
    return interpolated_df
