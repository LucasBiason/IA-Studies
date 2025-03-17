from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import PIL.Image

load_dotenv()

def generate(image_path):
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
    image = PIL.Image.open(image_path)
    text1 = """Dada a imagem de uma nota fiscal de compra, extraia os dados importantes dela e retorne no seguinte formato:
    - Empresa : nome da empresa que emitiu o recibo
    - Data: a data que foi feita a compra
    - CNPJ: cnpj da empresa que emitiu o recibo, sem pontuação
    - Tipo: tipo da despesa baseada nos itens comprados, escolha uma dentre as seguintes categorias:
                - Alimentação
                - Saúde
                - Mercado
                - Compras
                - Transporte
    - Itens: 
        - Descrição: nome ou descrição da mercadoria
        - Valor Unitário: valor unitário da mercadoria
        - Quantidade: quantidade da mercadoria
        - Valor Total: valor total da mercadoria
    - Valor Pago: valor pago
    Retorne os dados no formato JSON com nomes dos campos em snake_case."""

    model = "gemini-2.0-flash-001"
    generate_content_config = types.GenerateContentConfig(
        temperature = 1,
        top_p = 0.95,
        max_output_tokens = 8192,
        response_modalities = ["TEXT"],
    )
    response  = client.models.generate_content(
        model = model,
        contents = [text1, image],
        config = generate_content_config,
    )
    print(response.text)


print("== recibo001.png =================================")
generate('../recursos/images/recibo001.png')
print("== recibo002.png =================================")
generate('../recursos/images/recibo002.png')
print("== recibo003.png =================================")
generate('../recursos/images/recibo003.png')
print("== recibo004.png =================================")
generate('../recursos/images/recibo004.png')
print("== recibo005.png =================================")
generate('../recursos/images/recibo005.png')