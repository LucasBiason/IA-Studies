import os
import pytest
import pandas as pd
from app.model import HousePricePrediction
from unittest.mock import patch

@pytest.fixture
def house_price_model():
    model = HousePricePrediction()
    return model

def test_load_data(house_price_model):
    data = house_price_model.load_data()
    assert isinstance(data, pd.DataFrame)
    assert 'tamanho' in data.columns
    assert 'localizacao' in data.columns
    assert 'quantidade_quartos' in data.columns
    assert 'price' in data.columns

def test_train(house_price_model):
    house_price_model.train()
    assert os.path.exists(house_price_model.model_path)

def test_predict(house_price_model):
    house_price_model.train()
    features = [150, 'Vila', 4]
    prediction = house_price_model.predict(features)
    assert isinstance(prediction, float)

def test_predict_with_dataframe(house_price_model):
    house_price_model.train()
    features = pd.DataFrame([[150, 'Vila', 4]], columns=['tamanho', 'localizacao', 'quantidade_quartos'])
    prediction = house_price_model.predict(features)
    assert isinstance(prediction, float)

@patch('os.path.exists', return_value=False)
def test_predict_file_not_found(mock_exists, house_price_model):
    with pytest.raises(FileNotFoundError):
        features = [150, 'Vila', 4]
        house_price_model.predict(features)