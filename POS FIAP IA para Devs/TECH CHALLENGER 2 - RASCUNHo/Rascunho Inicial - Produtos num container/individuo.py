from random import random

class Individuo():
    def __init__(self, espacos, valores, limite_espacos, geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos
        self.nota_avaliacao = 0 # Soma dos valores que vao entrar no carregamento
        self.espaco_usado = 0 # Soma do espaço utilizado total
        self.geracao = geracao
        self.cromossomo = []
        
        for i in range(len(espacos)):
            if random() < 0.5: # 50% de probabilidade de levar o produto
                self.cromossomo.append("0") # Eu não vou levar
            else:
                self.cromossomo.append("1") # Eu vou levar
            
    def avaliacao(self):
        nota = 0
        soma_espacos = 0
        for i in range(len(self.cromossomo)):
           if self.cromossomo[i] == '1':
               nota += self.valores[i]
               soma_espacos += self.espacos[i]
        if soma_espacos > self.limite_espacos:
            nota = 1 # Se o somatorio for maior do que o limite de espaço ele superou o valor da carga
            # eu não posso carregar tudo, entao essa solução não é uma solução boa e assim
            # eu rebaixo a nota para 1 
        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos
    
    def crossover(self, outro_individuo):
        corte = round(random()  * len(self.cromossomo))
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1),
                  Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos
    
    def mutacao(self, taxa_mutacao):
        print("Antes %s " % self.cromossomo)
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
        print("Depois %s " % self.cromossomo)
        return self
        