import requests
from PyPDF2 import PdfReader 
from io import BytesIO
from tabula import read_pdf
# from libs import excelExport

def logicourse_pdf_backyard(url):
    # Get the PDF
    httprequest = requests.get(url)

    # First page of the PDF
    table_pdf = read_pdf(BytesIO(httprequest.content), stream=True, pages="all", multiple_tables=True)
    df = table_pdf[0]

    # Other pages of the PDF
    for i in range(1, len(table_pdf)):
        df = df.append(table_pdf[i])

    print(df)

    

logicourse_pdf_backyard("https://www.logicourse.fr/images/newsite/manifestations/pollionnay/pollionnay2023resu.pdf")