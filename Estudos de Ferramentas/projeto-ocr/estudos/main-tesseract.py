import pdfplumber
import re


pdf_path = '../recursos/pdfs/orçamento.pdf'

text = ''
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text += page.extract_text()

name_regex = r"Nome:\s*(\w+\s\w+)"
name = re.search(name_regex, text)

address_regex = r"Endereço:\s*([\w\s,\.]+[\d]+(?:\s?-\s?[A-Za-z\s]+(?:,\s?[A-Za-z\s]+)*\s?-\s?[A-Za-z]{2,})?)"
address = re.search(address_regex, text)

date_regex = r"Data:\s*(\d{2}/\d{2}/\d{4})"
date = re.search(date_regex, text)

total_regex = r"TOTAL\s*R\$\s*([\d.,]+)"
total = re.search(total_regex, text)

if name:
    print("Nome:", name.group(1))
else:
    print("Nome não encontrado")

if address:
    print("Endereço:", address.group(1))
else:
    print("Endereço não encontrado")

if date:
    print("Data:", date.group(1))
else:
    print("Data não encontrada")

if total:
    print("Valor Total:", total.group(1))
else:
    print("Valor Total não encontrado")
