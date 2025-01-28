import os
from flask import Flask, request, jsonify
from twilio.rest import Client
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client_twiilio = Client(account_sid, auth_token)

openai_key=os.environ.get("OPENAI_API_KEY")
client_openai = OpenAI(
    api_key=openai_key
)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.form
    body = data['Body'].lower()
    print(body)

    lista_mensagens = [
        {
            'role': 'system',
            'content': 'You are a helpful, upbeat and funny assistant.',
        },
        {"role": "user", "content": body}
    ]

    resposta = client_openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens,
        max_tokens=3000
    )

    # Enviar a resposta pelo WhatsApp
    client_twiilio.messages.create(
        body=resposta.choices[0].message.content,
        from_=f'whatsapp:{os.environ.get("TWILIO_NUMBER_FROM")}',
        to=f'whatsapp:{os.environ.get("TWILIO_NUMBER_TO")}'
    )

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(port=5000)