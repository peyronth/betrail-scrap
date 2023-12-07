import pandas as pd
import datetime
import os

def excel_export(df, file_name_suffixe):
    excel_file_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + file_name_suffixe + ".xlsx"
    export_folder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "export")
    excel_file_path = os.path.join(export_folder_path, excel_file_name)
    df.to_excel(excel_file_path, index=False, header=False)
    return excel_file_path