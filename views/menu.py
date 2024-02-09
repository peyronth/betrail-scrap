import tkinter as tk
import views.scrapfromurl as scrapfromurl
import views.scrapfromhtml as scrapfromhtml
import views.backyardinterpolation as backyardinterpolation
import views.backyardsplit as backyardsplit
from tkinter import ttk
import webbrowser

root = tk.Tk()

root.title('Race Scraper')
root.geometry('1000x200')

# Create the main frame
main_frame = ttk.Frame(root)
main_frame.pack(fill='both', expand=True)

# Create the menu
menu = tk.Menu(root)
root.config(menu=menu)

def scrap_url():
    global root
    scrapfromurl.scrapfromurl(root)

def scrap_html():
    global root
    scrapfromhtml.scrapfromhtml(root)

def backyard_smooth():
    global root
    backyardinterpolation.backyardinterpolation(root)

def backyard_split():
    global root
    backyardsplit.backyardsplit(root)

def see_compatibilities():
    # Open link 
    url = "https://github.com/peyronth/race-scrap/releases"
    webbrowser.open(url, new=2)


def display_home():
    global root
    # Select the main frame
    main_frame = root.winfo_children()[0]
    # Remove all children from the main frame
    for child in main_frame.winfo_children():
        child.destroy()
    main_frame.pack(fill='both', expand=True)
    show_home_view(main_frame)


def show_home_view(main_frame):
    # Create the content frame
    content_frame = ttk.Frame(main_frame)
    content_frame.pack(fill='both', expand=True)
    # Add your UI elements and navigation buttons to the content frame
    label = ttk.Label(content_frame, text="Welcome to the Race Scrap App!")
    label.pack(pady=20)
    button1 = ttk.Button(content_frame, text="Scrap Result from URL", command=scrap_url)
    button1.pack(pady=10)
    button2 = ttk.Button(content_frame, text="Scrap Result from HTML", command=scrap_html)
    button2.pack(pady=10)
    button3 = ttk.Button(content_frame, text="Smooth Backyard Results", command=backyard_smooth)
    button3.pack(pady=10)
    button31 = ttk.Button(content_frame, text="Split Backyard Results", command=backyard_split)
    button31.pack(pady=10)
    button4 = ttk.Button(content_frame, text="See Compatibilities", command=see_compatibilities)
    button4.pack(pady=10)


menu.add_command(label="Home", command=display_home)
scrap_submenu = tk.Menu(menu)
menu.add_cascade(label="Scrap", menu=scrap_submenu)
scrap_submenu.add_command(label="Scrap Result from URL", command=scrap_url)
scrap_submenu.add_command(label="Scrap Result from HTML", command=scrap_html)
backyard_submenu = tk.Menu(menu)
menu.add_cascade(label="Backyard", menu=backyard_submenu)
backyard_submenu.add_command(label="Backyard Smooth indexes", command=backyard_smooth)
backyard_submenu.add_command(label="Backyard Split indexes", command=backyard_split)
menu.add_command(label="See Compatibilities", command=see_compatibilities)


show_home_view(main_frame)

root.mainloop()
