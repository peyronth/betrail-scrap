# Build ui for the script selection
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from scriptlist import supportedHtmlFormats as supportedHtmlFormats
from tools.backyard.backyard import interpolate_race

def backyardinterpolation(root):
    # Select the main frame
    main_frame = root.winfo_children()[0]

    # Remove all children from the main frame
    for child in main_frame.winfo_children():
        child.destroy()
    
    # Change main frame to grid
    main_frame.grid(column=0, row=0, sticky='nsew')
    
    # Show the example url as a label
    example_url_label = ttk.Label(main_frame, text="Example format : ")
    example_url_label.grid(column=0, row=1)
    example_url_label.configure(state='readonly')

    example_url = ttk.Entry(main_frame, width=150)
    example_url.grid(column=1, row=1)
    example_url.insert(0, "https://www.betrail.run/race/parkinson.trail.tour/2023")
    example_url.configure(state='readonly')

    # Url text input
    url_entry = ttk.Entry(main_frame, width=150)
    url_entry.grid(column=1, row=3)
    url_entry_label = ttk.Label(main_frame, text="Enter the url")
    url_entry_label.grid(column=0, row=3)

    # Lap length float input
    lap_length_entry = ttk.Entry(main_frame, width=150)
    lap_length_entry.grid(column=1, row=4)
    lap_length_entry_label = ttk.Label(main_frame, text="Enter the lap length in km")
    lap_length_entry_label.grid(column=0, row=4)

    # Lap max duration string input (hh:mm:ss) default 60min
    lap_max_duration_entry = ttk.Entry(main_frame, width=150)
    lap_max_duration_entry.grid(column=1, row=5)
    lap_max_duration_entry.insert(0, "60")
    lap_max_duration_entry_label = ttk.Label(main_frame, text="Enter the lap max duration in minutes")
    lap_max_duration_entry_label.grid(column=0, row=5)

    # Title of race string input
    title_entry = ttk.Entry(main_frame, width=150)
    title_entry.grid(column=1, row=6)
    title_entry.insert(0, "Backyard")
    title_entry_label = ttk.Label(main_frame, text="Enter the title word that identify all your Backyard distances (For example if your distances are named Backyard 6h, Backyard 12h, Backyard 24h, enter Backyard)")
    title_entry_label.grid(column=0, row=6)


    # Create a button
    def clicked():
        race_infos = (url_entry.get().split("https://www.betrail.run/race/")[1]).split("/")
        race_name = race_infos[0]
        race_year = race_infos[1]
        url= "https://www.betrail.run/api/trail/" + race_name
        interpolate_race(url, race_year, float(lap_length_entry.get()), title_entry.get(), int(lap_max_duration_entry.get()))
        

    button = ttk.Button(main_frame, text="Validate", command=clicked)
    button.grid(column=1, row=7)

    # Display tkinter window
    main_frame.mainloop()