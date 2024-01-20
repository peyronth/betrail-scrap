import requests
from PyPDF2 import PdfReader 
from io import BytesIO
from tabula import read_pdf
import pandas as pd
import time
from libs import backyardSplit

def birth_refactor(reduced_year):
    if(reduced_year > 20):
        return '19' + str(reduced_year)
    elif(reduced_year < 10):
        return '200' + str(reduced_year)
    else:
        return '20' + str(reduced_year)


def logicourse_pdf_backyard(url):
    # Get the PDF
    httprequest = requests.get(url)

    # First page of the PDF
    table_pdf = read_pdf(BytesIO(httprequest.content), stream=True, pages="all", multiple_tables=True)
    df = table_pdf[0]

    # Other pages of the PDF
    for i in range(1, len(table_pdf)):
        df = df.append(table_pdf[i])    

    # Reset index
    df = df.reset_index(drop=True)

    df['gender'] = df['Clt Sx'].apply(lambda x: 'M' if 'M' in str(x) else 'F')
    df['Né'] = df['Né'].apply(lambda x: birth_refactor(x))

    return backyardSplit.exportbylapcount(df, "Nb Tr Retenus")
