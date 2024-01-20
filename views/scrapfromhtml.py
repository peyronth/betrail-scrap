# Build ui for the script selection
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from scriptlist import supportedHtmlFormats as supportedHtmlFormats

def scrapfromhtml(root):
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
    example_url.configure(state='readonly')

    # Update the example url when the dropdown is changed
    def update_example_url(*args):
        example_url.configure(state='normal')
        example_url.delete(0, tk.END)
        example_url.insert(0, supportedHtmlFormats[selected_website.get()]['exampleFormat'])
        example_url.configure(state='readonly')

    # Create a select dropdown
    selected_website = tk.StringVar()
    selected_website.set('Select a website')
    website_label = ttk.Label(main_frame, text="Select a website")
    website_label.grid(column=0, row=2)
    website_dropdown = ttk.OptionMenu(main_frame, selected_website, "Select a website", *supportedHtmlFormats.keys(), command=update_example_url)
    website_dropdown.grid(column=1, row=2)


    # Create a button
    def clicked():
        if(selected_website.get() == 'Select a website'):
            messagebox.showerror('Error', 'Please select a website')
            return
        filename = filedialog.askopenfilename()
        html = open(filename, 'r', encoding='utf-8').read()
        # Launch the script
        returned_paths = supportedHtmlFormats[selected_website.get()]["script"](html)
        # Check if the file is created
        if isinstance(returned_paths, list):
            messagebox.showinfo('Success', 'File created at ' + ', '.join(returned_paths))
        else:
            messagebox.showerror('Error', 'An error occured')
        

    button = ttk.Button(main_frame, text="Choose HTML File", command=clicked)
    button.grid(column=1, row=7)

    # Display tkinter window
    main_frame.mainloop()