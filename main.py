import os

def create_export_folder():
    export_folder = 'export'
    os.makedirs(export_folder, exist_ok=True)

if __name__ == "__main__":
    create_export_folder()

import views.menu as menu