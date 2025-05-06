# Tech Challenger 

Este projeto é um desafio técnico feito como conclusão do primeiro módulo do curso Pós Tech - IA para Devs para a FIAP.
Consiste na construção de um módelo preditivo de uma base de dados utilizando so conhecimentos do curso.

**Problema:**
Você é um(a) profissional encarregado(a) de desenvolver um modelo
preditivo de regressão para prever o valor dos custos médicos individuais
cobrados pelo seguro de saúde.

## Projeto de Análise

Esta fase consiste em escolher a base de dados que iremos trabalha, fazer a exploração das caracteristicas assim como uma analise dos dados. Após isso construir o modelo de previsão dos custos médicos.

Os arquivos referentes a esta fase estão na pasta **analise**.

### Etapa 01 - Análise e Preparação dos Dados

Nesta etapa estamos fazendo analise do conjunto de dados para aprender o máximo possível sobre ele, assim como o que podemos extrair de informações.
O foco é em preparar os dados para os modelos de dados.

### Etapa 02 - Construção do Modelo Preditivo

Nesta etapa vamos aproveitar a limpeza dos dados e tratamento de valores que foi feita na etapa anterior e criar um modelo preditivo de regressão utilizando algumas técnicas e verificar o que fica melhor para a distruição dos dados.

## Projeto Entregável

Esta fase consiste em criar um pacote utilizavel com o modelo preditivo realizado na primeira parte do desafio.

Os arquivos referentes a esta fase estão na pasta **projeto**.

### Painel Relatório

Utilizaremos o framework Streamlit do python para criar um dashboard com o dados e analise feita na fase anterior.

### Microserviço de Previsão

Utilizaremos a estrutura de um microserviço em FAST API para entregar uma forma de utilização para o modelo, onde o cliente do serviço fará uma requisição com os dados e receberá o charge previsto.