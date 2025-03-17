import os
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

class HousePricePrediction:
    def __init__(self):
        self.model_path = 'model.pkl'
        self.pipeline = None

    def load_data(self):
        data = pd.read_csv('data/house_prices.csv', sep='|')
        return data

    def train(self):
        data = self.load_data()
        X = data.drop('price', axis=1)
        y = data['price']
        
        # Criar o pré-processador passando transformadores para normalização e codificação     
        # e colunas para normalização e codificação
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), ['tamanho', 'quantidade_quartos']), # numeric features
                ('cat', OneHotEncoder(), ['localizacao']) # categorical features
            ])
        
        # Criar o pipeline com o pré-processador e o modelo
        self.pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                        ('model', LinearRegression())])
        
        # Dividir os dados em conjuntos de treinamento e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Treinar o pipeline
        self.pipeline.fit(X_train, y_train)
        
        # Salvar o pipeline treinado
        with open(self.model_path, 'wb') as f:
            pickle.dump(self.pipeline, f)

    def predict(self, features):
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file '{self.model_path}' not found. Please train the model first.")
        
        with open(self.model_path, 'rb') as f:
            self.pipeline = pickle.load(f)
        
        if not isinstance(features, pd.DataFrame):
            features = pd.DataFrame([features], columns=['tamanho', 'localizacao', 'quantidade_quartos'])
        
        prediction = self.pipeline.predict(features)
        return round(float(prediction[0]), 2)