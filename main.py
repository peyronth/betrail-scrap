import os
from scriptlist import supportedWebsites as supportedWebsites

def create_export_folder():
    export_folder = 'export'
    os.makedirs(export_folder, exist_ok=True)

if __name__ == "__main__":
    create_export_folder()


# Build ui for the script selection
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create the window
tkWindow = tk.Tk()
tkWindow.title('Race Scraper')
tkWindow.geometry('1000x120')

# Set text alignment to center
tkWindow.option_add('*justify', 'center')

# Show the example url as a label
exampleUrlLabel = ttk.Label(tkWindow, text="Example url : ")
exampleUrlLabel.grid(column=0, row=2)
exampleUrl = ttk.Label(tkWindow, width=160)
exampleUrl.grid(column=1, row=2)

# Update the example url when the dropdown is changed
def update_example_url(*args):
    exampleUrl.config(text=supportedWebsites[selectedWebsite.get()]["exampleUrl"])

# Create a select dropdown
selectedWebsite = tk.StringVar()
selectedWebsite.set('Select a website')
websiteLabel = ttk.Label(tkWindow, text="Select a website")
websiteLabel.grid(column=0, row=0)
websiteDropdown = ttk.OptionMenu(tkWindow, selectedWebsite, "Select a website", *supportedWebsites.keys(), command=update_example_url)
websiteDropdown.grid(column=1, row=0)

# Create a text entry box
urlEntry = ttk.Entry(tkWindow, width=80)
urlEntry.grid(column=1, row=4)
urlEntryLabel = ttk.Label(tkWindow, text="Enter the url")
urlEntryLabel.grid(column=0, row=4)

# Create a button
def clicked():
    if(selectedWebsite.get() == 'Select a website'):
        messagebox.showerror('Error', 'Please select a website')
        return
    if urlEntry.get() == '':
        messagebox.showerror('Error', 'Please enter an url')
    else:
        # Launch the script
        returned_path = supportedWebsites[selectedWebsite.get()]["script"](urlEntry.get())
        # Check if the file is created
        if isinstance(returned_path, str):
            messagebox.showinfo('Success', 'File created at ' + returned_path)
        else:
            messagebox.showerror('Error', 'An error occured')

button = ttk.Button(tkWindow, text="Launch", command=clicked)
button.grid(column=1, row=6)

# Display tkinter window
tkWindow.mainloop()