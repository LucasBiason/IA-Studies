from datetime import datetime
from llm_client import LLMClient


class TransactionsClassifier:
    
    def __init__(self, df, pathfile):
        self.df = df
        self.client = LLMClient()
        self.pathfile = pathfile
    
    def classify(self):
        categorias = []
        for descricao in list(self.df["Descrição"].values):
            prompt = f"""
                Você é um analista de dados, trabalhando em um projeto de limpeza de dados.
                Seu trabalho é escolher uma categoria adequada para cada lançamento financeiro
                que vou te enviar.

                Todos são transações financeiras de uma pessoa física.

                Escolha uma dentre as seguintes categorias:
                - Alimentação
                - Receitas
                - Saúde
                - Mercado
                - Saúde
                - Educação
                - Compras
                - Transporte
                - Investimento
                - Transferências para terceiros
                - Telefone
                - Moradia

                Escola a categoria deste item:
                {descricao}

                Responda apenas com a categoria.
                """
            print(prompt)
            resposta = self.client.send_message(prompt)
            print(resposta)
            categorias.append(resposta)
        
        self.df["Categoria"] = categorias
        self.df = self.df[self.df["Data"] >= datetime(2024, 3, 1).date()]
        self.df.to_csv(self.pathfile)