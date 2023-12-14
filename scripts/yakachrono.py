import requests
from PyPDF2 import PdfReader 
from io import BytesIO
from tabula import read_pdf
from libs import excelExport

def yakachrono_pdf(url):
    # Get the PDF
    httprequest = requests.get(url)

    # First page of the PDF
    table_pdf_firstpage = read_pdf(BytesIO(httprequest.content), stream=True, pages="all", area=(100, 0, 820, 999999999), multiple_tables=True, pandas_options={'header': None})
    table = table_pdf_firstpage[0]

    # Other pages of the PDF
    table_pdf_otherpage = read_pdf(BytesIO(httprequest.content), stream=True, pages="all", area=(40, 0, 820, 999999999), multiple_tables=True, pandas_options={'header': None})
    for i in range(1, len(table_pdf_otherpage)):
        table = table.append(table_pdf_otherpage[i])

    # Reset index
    table = table.reset_index(drop=False)

    # Get gender if column 8 contains "H/" M else F
    table['Gender'] = table[8].apply(lambda x: 'M' if 'H/' in str(x) else 'F')

    # Convert column 5 from %Hh%M'%S" to %H:%M:%S
    table[5] = table[5].apply(lambda x: x.replace("h", ":").replace("'", ':'))

    # For column 5 if contains only %M:%S" add 00:
    table[5] = table[5].apply(lambda x: '0:' + x if len(x) == 5 else x)

    # Keep columns 0, 1, 2, 3, 5, and "Gender"
    table = table[[0, 1, 2, 3, 5, "Gender"]]

    return [excelExport.excel_export(table, "yakachrono")]

    

yakachrono_pdf("https://www.ganatrail.com/_files/ugd/a39524_982ab77c9b054edc83fe4b4085e22de6.pdf")