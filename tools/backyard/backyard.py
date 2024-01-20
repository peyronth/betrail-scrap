import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scripts.betrail import betrail_backyard_getperformance
import tkinter as tk
from tkinter import ttk
import math as Math

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
    performances_df['interpolation'] = performances_df[['linear_interpolation', 'power_interpolation']].mean(axis=1)

    return performances_df

def compute_index(interpolated_df, race_lap_time=60):
    constant = 0.864
    # Compute index
    interpolated_df['index'] = round(interpolated_df['lap_count'] * interpolated_df['interpolation'] * (race_lap_time*60)/100/constant, 0)
    return interpolated_df

def interpolate_race(url, year, lap_length, string_to_contain="", lap_duration=60):
    performances_df = betrail_backyard_getperformance(url, year, lap_length, string_to_contain)
    interpolated_df = interpolate_selected_perf(performances_df)
    new_index_df = compute_index(interpolated_df, lap_duration)

    # Create a tkinter window
    window = tk.Tk()

    # Create a treeview widget
    tree = ttk.Treeview(window)

    # Define the columns
    tree["columns"] = ("lap_count", "distance", "old_index", "index")

    # Format the columns
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("lap_count", anchor=tk.CENTER, width=100)
    tree.column("distance", anchor=tk.CENTER, width=100)
    tree.column("old_index", anchor=tk.CENTER, width=100)
    tree.column("index", anchor=tk.CENTER, width=100)

    # Create the column headings
    tree.heading("#0", text="", anchor=tk.CENTER)
    tree.heading("lap_count", text="lap count", anchor=tk.CENTER)
    tree.heading("distance", text="distance", anchor=tk.CENTER)
    tree.heading("old_index", text="old index", anchor=tk.CENTER)
    tree.heading("index", text="new index", anchor=tk.CENTER)

    # Insert the data into the treeview
    for i, row in new_index_df.iterrows():
        tree.insert("", tk.END, text="", values=(row["lap_count"], row['distance'], row["old_index"], row["index"]))

    def your_copy():
        item = tree.selection()[0]
        content = Math.ceil(float(tree.item(item)["values"][-1]))
        window.clipboard_clear()
        window.clipboard_append(content)

    def popup_menu(event):
        id_row = tree.identify_row(event.y)
        if id_row:
            tree.selection_set(id_row)
        popup1.post(event.x_root, event.y_root)

    # Make index column cells copyable
    popup1 = tk.Menu(tree, tearoff=0)
    popup1.add_command(
        command=your_copy,
        label="Copy")
    tree.bind('<Button-3>', popup_menu)

    # display scrollbar on tree
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # Add a button which show the interpolated plots
    def show_plots():
        show_interpolated_plots(interpolated_df, new_index_df)
    
    button = ttk.Button(window, text="Show interpolated plots diagrams", command=show_plots)
    button.pack()

    # Start the tkinter event loop
    window.mainloop()

def show_interpolated_plots (interpolated_df, new_index_df):
    # Plot interpolated_df['selected_prono'] as points with two unnterpolation interpolated_df['linear_interpolation'] and interpolated_df['power_interpolation'] as lines with on x axis lap_count
    plt.subplot(1, 2, 1)
    plt.plot(interpolated_df['lap_count'], interpolated_df['selected_prono'], 'o', label='raw prono', color='grey')
    plt.plot(interpolated_df['lap_count'], interpolated_df['linear_interpolation'], label='linear interpolation', color='yellow')
    plt.plot(interpolated_df['lap_count'], interpolated_df['power_interpolation'], label='power interpolation', color='orange')
    plt.plot(interpolated_df['lap_count'], interpolated_df['interpolation'], 'o--', label='interpolated prono', color='green')
    plt.legend()
    plt.grid(True)

    # Plot new_index_df['old_index'] against new_index_df['index']
    plt.subplot(1, 2, 2)
    plt.plot(new_index_df['lap_count'], new_index_df['old_index'], 'o--', label='raw index', color='grey')
    plt.plot(new_index_df['lap_count'], new_index_df['index'], label='new index', color='green')
    plt.legend()
    plt.grid(True)

    plt.show()
