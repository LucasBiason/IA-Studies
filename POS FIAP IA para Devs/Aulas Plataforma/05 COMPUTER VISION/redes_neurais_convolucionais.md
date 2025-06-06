# Aula 04 - Redes Neurais Convolucionais (CNN)

## Introdução

Redes Neurais Convolucionais (CNNs) são uma classe de redes neurais muito eficazes para tarefas de visão computacional, como classificação de imagens, detecção de objetos e segmentação. Elas são inspiradas no funcionamento do córtex visual animal e são capazes de extrair automaticamente características relevantes das imagens.

---

## 1. Importando Bibliotecas

```python
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
```

**Explicação:**

- `numpy`: Biblioteca para operações matemáticas e manipulação de arrays.
- `matplotlib.pyplot`: Usada para visualização de imagens e gráficos.
- `tensorflow.keras.datasets`: Permite importar conjuntos de dados prontos, como o MNIST.
- `to_categorical`: Converte rótulos inteiros em vetores one-hot.
- `Sequential`: Modelo sequencial do Keras, onde as camadas são empilhadas linearmente.
- `Conv2D`: Camada convolucional bidimensional.
- `MaxPooling2D`: Camada de pooling para reduzir a dimensionalidade.
- `Flatten`: Achata a entrada para uma dimensão.
- `Dense`: Camada totalmente conectada.
- `Dropout`: Técnica para evitar overfitting.

---

## 2. Carregando e Preparando os Dados

```python
# Carregar o dataset MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Visualizar algumas imagens
plt.figure(figsize=(10,4))
for i in range(6):
    plt.subplot(1,6,i+1)
    plt.imshow(X_train[i], cmap='gray')
    plt.title(f"Label: {y_train[i]}")
    plt.axis('off')
plt.show()
```

**Explicação:**

- O MNIST é um conjunto de dados de dígitos manuscritos (0 a 9), com 60.000 imagens para treino e 10.000 para teste.
- Cada imagem tem 28x28 pixels em escala de cinza.
- O código acima carrega os dados e mostra as 6 primeiras imagens do conjunto de treino, junto com seus rótulos.

---

## 3. Pré-processamento dos Dados

```python
# Redimensionar para (28, 28, 1) e normalizar os valores dos pixels
X_train = X_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
X_test = X_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0

# Converter os rótulos para one-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
```

**Explicação:**

- `reshape(-1, 28, 28, 1)`: Adiciona um canal (1) para indicar que as imagens são em escala de cinza.
- `astype('float32') / 255.0`: Normaliza os valores dos pixels para o intervalo [0, 1], o que ajuda no treinamento.
- `to_categorical`: Converte os rótulos de inteiros para vetores one-hot, necessários para classificação multiclasse.

---

## 4. Construindo a CNN

```python
model = Sequential()

# Primeira camada convolucional
model.add(Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)))
model.add(MaxPooling2D((2,2)))

# Segunda camada convolucional
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D((2,2)))

# Achatar e adicionar camadas densas
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))  # Dropout para evitar overfitting
model.add(Dense(10, activation='softmax'))  # 10 classes

# Resumo do modelo
model.summary()
```

**Explicação:**

- **Conv2D**: Aplica filtros convolucionais para extrair características locais da imagem.
    - 32 filtros na primeira camada, 64 na segunda.
    - Filtros de tamanho 3x3.
    - Função de ativação ReLU (Rectified Linear Unit).
- **MaxPooling2D**: Reduz a dimensionalidade (downsampling), mantendo as características mais importantes.
- **Flatten**: Achata a saída das camadas convolucionais para uma dimensão.
- **Dense**: Camada totalmente conectada, usada para classificação.
- **Dropout**: Desativa aleatoriamente 50% dos neurônios durante o treinamento para evitar overfitting.
- **Softmax**: Função de ativação para classificação multiclasse.

---

## 5. Compilando o Modelo

```python
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
```

**Explicação:**

- **optimizer='adam'**: Otimizador eficiente para redes neurais.
- **loss='categorical_crossentropy'**: Função de perda para classificação multiclasse.
- **metrics=['accuracy']**: Métrica de avaliação.

---

## 6. Treinando o Modelo

```python
history = model.fit(X_train, y_train,
                    epochs=10,
                    batch_size=128,
                    validation_split=0.2)
```

**Explicação:**

- **epochs=10**: Número de vezes que o modelo verá todo o conjunto de dados de treino.
- **batch_size=128**: Número de amostras por atualização do gradiente.
- **validation_split=0.2**: 20% dos dados de treino serão usados para validação.

---

## 7. Avaliando o Modelo

```python
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")
```

**Explicação:**

- Avalia o desempenho do modelo nos dados de teste, que não foram vistos durante o treinamento.

---

## 8. Visualizando o Treinamento

```python
plt.plot(history.history['accuracy'], label='Acurácia Treino')
plt.plot(history.history['val_accuracy'], label='Acurácia Validação')
plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.legend()
plt.show()
```

**Explicação:**

- Mostra como a acurácia evolui durante o treinamento e validação, ajudando a identificar overfitting ou underfitting.

---

## 9. Fazendo Previsões

```python
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test, axis=1)

# Exibir algumas previsões
plt.figure(figsize=(10,4))
for i in range(6):
    plt.subplot(1,6,i+1)
    plt.imshow(X_test[i].reshape(28,28), cmap='gray')
    plt.title(f"P: {predicted_classes[i]}\nV: {true_classes[i]}")
    plt.axis('off')
plt.show()
```

**Explicação:**

- O modelo faz previsões nas imagens de teste.
- `np.argmax` retorna a classe com maior probabilidade.
- As primeiras 6 imagens de teste são exibidas com a previsão do modelo (P) e o valor verdadeiro (V).

---

## Conclusão

Nesta aula, aprendemos:

- O que são redes neurais convolucionais (CNNs) e por que são importantes para visão computacional.
- Como carregar e pré-processar dados de imagens.
- Como construir, treinar e avaliar uma CNN simples usando Keras/TensorFlow.
- Como visualizar os resultados e interpretar as previsões do modelo.

---

## Exemplos de Aplicações de IA

1. **Reconhecimento de Imagens e Vídeos**  
   - Identificação de objetos, pessoas, animais, etc.
   - Diagnóstico médico por imagem (ex: detecção de tumores em radiografias).

2. **Processamento de Linguagem Natural (PLN)**  
   - Tradução automática (Google Tradutor).
   - Chatbots e assistentes virtuais (Siri, Alexa).
   - Análise de sentimentos em textos.

3. **Reconhecimento de Voz**  
   - Conversão de fala em texto.
   - Comandos de voz para dispositivos.

4. **Previsão e Análise de Dados**  
   - Previsão do tempo.
   - Previsão de preços de ações.
   - Detecção de fraudes em transações financeiras.

5. **Jogos e Entretenimento**  
   - Inteligência artificial em jogos (ex: AlphaGo).
   - Criação de músicas, imagens e textos (redes generativas).

6. **Robótica e Veículos Autônomos**  
   - Direção autônoma de carros.
   - Controle de robôs industriais.

7. **Saúde**  
   - Diagnóstico de doenças.
   - Descoberta de novos medicamentos.

8. **Agricultura**  
   - Monitoramento de plantações por imagens de satélite.
   - Detecção de pragas.

9. **Segurança**  
   - Reconhecimento facial.
   - Detecção de intrusos em sistemas.

10. **Personalização**  
    - Recomendação de produtos (Netflix, Amazon).
    - Filtragem de spam em e-mails.