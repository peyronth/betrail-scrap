# Build ui for the script selection
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from libs.backyardSplit import excelsplitdistance, excelsplitlapcount

def backyardsplit(root):
    # Select the main frame
    main_frame = root.winfo_children()[0]

    # Remove all children from the main frame
    for child in main_frame.winfo_children():
        child.destroy()
    
    # Change main frame to grid
    main_frame.grid(column=0, row=0, sticky='nsew')
    
    # Excel file selection
    excel_file_path = filedialog.askopenfilename()
    excel_file_label = ttk.Label(main_frame, text=excel_file_path)
    excel_file_label.grid(column=0, row=1)
    excel_file_label.configure(state='readonly')

    # Name of the split column
    split_column_entry = ttk.Entry(main_frame, width=150)
    split_column_entry.grid(column=1, row=2)
    split_column_entry_label = ttk.Label(main_frame, text="Enter the name of the column to split")
    split_column_entry_label.grid(column=0, row=2)

    # button split by distance
    def split_by_distance():
        result_array = excelsplitdistance(excel_file_path, split_column_entry.get())
        messagebox.showinfo('Success', 'Files created at ' + ', '.join(result_array))
    split_by_distance_button = ttk.Button(main_frame, text="Split by distance", command=split_by_distance)
    split_by_distance_button.grid(column=0, row=3)

    # button split by lap count
    def split_by_lap_count():
        result_array = excelsplitlapcount(excel_file_path, split_column_entry.get())
        messagebox.showinfo('Success', 'Files created at ' + ', '.join(result_array))
    split_by_lap_count_button = ttk.Button(main_frame, text="Split by lap count", command=split_by_lap_count)
    split_by_lap_count_button.grid(column=1, row=3)
