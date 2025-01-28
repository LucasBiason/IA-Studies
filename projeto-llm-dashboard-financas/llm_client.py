import requests


class LLMClient:
    def __init__(self, base_url="http://localhost:11434/api/generate"):
        self.base_url = base_url

    def send_message(self, message):
        payload = {
            "model": "llama3",
            "stream": False,
            "prompt": message
        }
        try:
            response = requests.post(self.base_url, json=payload)
            response.raise_for_status() # status HTTP 4xx/5xx
            response = response.json()
            return response["response"]
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None

