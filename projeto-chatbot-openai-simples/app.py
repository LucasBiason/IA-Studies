import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        # Role: user = usuário, chatbot = chatbot, assistant = assistente
        # orientações gerais podemos passar role como system
        {"role": "user", "content": mensagem}
    )

    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens,
    )
    return resposta.choices[0].message

lista_mensagens = []
while True:
    texto = input("Escreva aqui sua mensagem:")

    if texto.lower() == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append(resposta)
        print("Chatbot:", resposta.content)