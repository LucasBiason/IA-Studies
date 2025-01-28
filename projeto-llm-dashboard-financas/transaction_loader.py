import pandas as pd


class TransactionLoader:
    
    def __init__(self, path):
        df = pd.read_csv(path)
        del df["ID"]
        df["Mês"] = df["Data"].apply(lambda x: "-".join(x.split("-")[:-1]))
        df["Data"] = pd.to_datetime(df["Data"])
        df["Data"] = df["Data"].apply(lambda x: x.date())
        df = df[df["Categoria"]!="Receitas"]
        df["Valor"] = df["Valor"].abs()
        self.df = df

    def filter_data(self, mes, selected_categories):
        df_filtered = self.df[self.df['Mês'] == mes]
        if selected_categories:
            df_filtered = df_filtered[df_filtered['Categoria'].isin(selected_categories)]
        return df_filtered
    
    def mounth_filters(self):
        return self.df["Mês"].unique().tolist()
    
    def category_filters(self):
        return self.df["Categoria"].unique().tolist()