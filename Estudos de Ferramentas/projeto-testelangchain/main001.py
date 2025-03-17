import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import OllamaLLM

from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Invoke Simples da LLM
model = ChatOpenAI(model='gpt-3.5-turbo')
#model = OllamaLLM(model="llama3")

messages = [
    # SystemMessage uma diretriz, um contexto que explica pra IA como ela deve se comportar
    SystemMessage(content="Você é um assistente que fornece informações sobre figuras históricas."),
]

while True:
    question = input('O que deseja saber? ')
    if question == 'sair':
        break

    # HumanMessage é a mensagem que o usuário enviaria para a IA
    messages.append(HumanMessage(content=question))
    response = model.invoke(messages)
    print(response)

    # AIMessage é a mensagem que a IA responderia ao usuário
    messages.append(AIMessage(content=response.content))