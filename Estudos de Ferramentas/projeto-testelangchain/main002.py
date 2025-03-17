import os
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Invoke Simples da LLM
model = ChatOpenAI(model='gpt-3.5-turbo')

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content='Você deve responder baseado em dados geográficos de regiões do Brasil.'
        ),
        HumanMessagePromptTemplate.from_template(
            template='Por favor, me fale sobre a região {regiao}.'
        ),
        AIMessage(
            content='Claro, vou começar coletando informações sobre a região e analisando os dados disponíveis.'
        ),
        HumanMessage(
            content='Certifique-se de incluir dados demográficos.'
        ),
        AIMessage(
            content='Entendido. Aqui estão os dados:'
        ),
    ]
)

while True:
    regiao = input('Sobre qual região deseja saber? ')
    if regiao == 'sair':
        break

    prompt = chat_template.format_messages(regiao=regiao)
    print(prompt)

    response = model.invoke(prompt)
    print(response.content)
