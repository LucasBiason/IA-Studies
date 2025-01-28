import ofxparse
import pandas as pd
import os


class TransactionsExtractor:
    
    def __init__(self, path):
        self.path = path
        self.df = pd.DataFrame()
    
    def extract(self):
        for extrato in os.listdir(self.path):
            with open(f'{self.path}/{extrato}', encoding='ISO-8859-1') as ofx_file:
                ofx = ofxparse.OfxParser.parse(ofx_file)
            transactions_data = []

            for account in ofx.accounts:
                for transaction in account.statement.transactions:
                    transactions_data.append({
                        "Data": transaction.date,
                        "Valor": transaction.amount,
                        "Descrição": transaction.memo,
                        "ID": transaction.id,
                    })

            df_temp = pd.DataFrame(transactions_data)
            df_temp["Valor"] = df_temp["Valor"].astype(float)
            df_temp["Data"] = df_temp["Data"].apply(lambda x: x.date())
            self.df = pd.concat([self.df, df_temp])
        self.df = self.df.set_index("ID")