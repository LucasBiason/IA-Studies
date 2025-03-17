# House Price Prediction

## Objetivo

O objetivo deste projeto é prever os preços das casas com base em várias características, como tamanho, localização, número de quartos, entre outros. Utilizamos algoritmos de aprendizado de máquina para criar um modelo preditivo que pode estimar o preço de uma casa com base nesses atributos.

## Instalação

### Pré-requisitos

Certifique-se de ter os seguintes softwares instalados em sua máquina:

- [Python 3.8+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)

### Passo a Passo

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/projects-ia-house-price-prediction.git
    cd projects-ia-house-price-prediction
    ```

2. **Crie e ative um ambiente virtual:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. **Instale as dependências do projeto:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Execute a aplicação usando Docker:**

    ```bash
    make runapp-dev
    ```

5. **Acesse a API:**

    A API estará disponível em `http://localhost:5000`.

6. **Treine e teste o modelo:**

    Siga os exemplos de uso da API fornecidos na seção anterior para treinar e testar o modelo.


## Uso da API

1. Inicie o servidor:
    ```bash
    python app.py
    ```

2. Faça uma requisição para a API:
    ```bash
    curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{
        "tamanho": 120,
        "localizacao": "Centro",
        "quantidade_quartos": 3
    }'
    ```

3. Exemplo de resposta:
    ```json
    {
        "preco": 450000
    }
    ```

## Contribuição
Sinta-se à vontade para contribuir com este projeto. Para isso, faça um fork do repositório, crie uma nova branch com sua feature ou correção de bug, e envie um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.