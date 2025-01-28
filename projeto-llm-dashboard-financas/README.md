
# Pré-requisitos:

Colocar extrato bancário na pasta "extratos" no formato .ofx


# Rodando Llhama Localmente via Docker:

docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

docker exec -it ollama ollama run llama3


# Teste de execução do Llhama Local:
```
curl --request POST \
  --url http://localhost:11434/api/generate \
  --header 'Content-Type: application/json' \
  --data '{
  "model": "llama3",
	"stream": false,
  "prompt": "Olá, como você está?"
}'
```

# Criando o arquivo .csv:
```
python setup.py
```

# Executando o Dashboard:
```
streamlit run app.py
```
