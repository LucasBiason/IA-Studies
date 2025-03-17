import pytesseract

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from pdf2image import convert_from_path


load_dotenv()

pdf_path = '../recursos/pdfs/orçamento_img.pdf'

pages = convert_from_path(
    pdf_path=pdf_path,
)

text_data = ''
for page in pages:
    text = pytesseract.image_to_string(page)
    text_data += text + '\n'

llm = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0,
)

template = """
Extraia e retorne as informações mais relevantes do texto fornecido:

Retorne os dados no formato JSON com nomes dos campos em snake_case.
{text}
"""

prompt = PromptTemplate(
    input_variables=['text'],
    template=template,
)

chain = prompt | llm | JsonOutputParser()

response = chain.invoke({'text': text})

print(response)
