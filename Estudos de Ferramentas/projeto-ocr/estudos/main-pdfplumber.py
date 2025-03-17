import pdfplumber


pdf_path = '../recursos/pdfs/orçamento.pdf'

def extrair_texto(page):
    return page.extract_text()

def extrair_tabelas(page):
    tables = []
    for table in page.extract_tables():
        for row in table:
            tables.append(row)
    return tables   

def percorrer_paginas(pdf_path):
    texts = ''
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += extrair_texto(page)
            tables += extrair_tabelas(page)
            
    print(texts)
    print(tables)
    return texts, tables


percorrer_paginas(pdf_path)
