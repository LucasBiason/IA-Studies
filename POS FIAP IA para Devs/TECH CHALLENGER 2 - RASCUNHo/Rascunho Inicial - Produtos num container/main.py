from produtos import Produto
from individuo import Individuo
from algoritmo_genetico import AlgoritmoGenetico
import matplotlib.pyplot as plt


if __name__ == '__main__':
    lista_produtos = []
    lista_produtos.append(Produto("Geladeira Dako", 0.751, 999.90))
    lista_produtos.append(Produto("Iphone 6", 0.0000899, 2911.12))
    lista_produtos.append(Produto("TV 55' ", 0.400, 4346.99))
    lista_produtos.append(Produto("TV 50' ", 0.290, 3999.90))
    lista_produtos.append(Produto("TV 42' ", 0.200, 2999.00))
    lista_produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
    lista_produtos.append(Produto("Ventilador Panasonic", 0.496, 199.90))
    lista_produtos.append(Produto("Microondas Electrolux", 0.0424, 308.66))
    lista_produtos.append(Produto("Microondas LG", 0.0544, 429.90))
    lista_produtos.append(Produto("Microondas Panasonic", 0.0319, 299.29))
    lista_produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
    lista_produtos.append(Produto("Geladeira Consul", 0.870, 1199.89))
    lista_produtos.append(Produto("Notebook Lenovo", 0.498, 1999.90))
    lista_produtos.append(Produto("Notebook Asus", 0.527, 3999.00))
    for produto in lista_produtos:
        print(produto.nome)
        
    # Gerando os Individuos
    espacos = []
    valores = []
    nomes = []
    for produto in lista_produtos:
        espacos.append(produto.espaco)
        valores.append(produto.valor)
        nomes.append(produto.nome)
    limite = 3
    
    individuo1 = Individuo(espacos, valores, limite)
    print("Espaços = %s" % str(individuo1.espacos))
    print("Valores = %s" % str(individuo1.valores))
    print("Cromossomo = %s" % str(individuo1.cromossomo))
    
    print("\nComponentes da carga")
    for i in range(len(lista_produtos)):
        if individuo1.cromossomo[i] == '1':
            print("Nome: %s R$ %s " % (lista_produtos[i].nome, lista_produtos[i].valor))
    
    individuo1.avaliacao()
    print("Nota = %s" % individuo1.nota_avaliacao)
    print("Espaço usado = %s" % individuo1.espaco_usado)
    
    individuo2 = Individuo(espacos, valores, limite)
    print("\nIndivíduo 2")
    for i in range(len(lista_produtos)):
        if individuo2.cromossomo[i] == '1':
            print("Nome: %s R$ %s " % (lista_produtos[i].nome, lista_produtos[i].valor))
    individuo2.avaliacao()
    print("Nota = %s" % individuo2.nota_avaliacao)
    print("Espaço usado = %s" % individuo2.espaco_usado)
    
    individuo1.crossover(individuo2)
    
    individuo1.mutacao(0.05)
    individuo2.mutacao(0.05)
    print("\n"*8)

    tamanho_populacao = 200
    ag = AlgoritmoGenetico(tamanho_populacao)
    ag.inicializa_populacao(espacos, valores, limite)
    for individuo in ag.populacao:
        individuo.avaliacao()
    ag.ordena_populacao()
    ag.melhor_individuo(ag.populacao[0]) 
    # quanto eu faço a ordenação, o melhor individuo fica sempre em primeiro
    soma = ag.soma_avaliacoes()
    print("Soma das avaliações: %s" % soma)
    
    nova_populacao = []
    probabilidade_mutacao = 0.01
    for individuos_gerados in range(0, ag.tamanho_populacao, 2):
        # Vamos gerar dois pais de uma vez para o crossover
        pai1 = ag.seleciona_pai(soma)
        pai2 = ag.seleciona_pai(soma)
        
        filhos = ag.populacao[pai1].crossover(ag.populacao[pai2])
        nova_populacao.append(filhos[0].mutacao(probabilidade_mutacao))
        nova_populacao.append(filhos[1].mutacao(probabilidade_mutacao))
        
    ag.populacao = list(nova_populacao)
    for individuo in ag.populacao:
        individuo.avaliacao()
    ag.ordena_populacao()
    ag.melhor_individuo(ag.populacao[0])        
    soma = ag.soma_avaliacoes()
    
    print("*** Melhor Solução para o Problema:****\n",
            "Espaços = %s\n" % str(ag.melhor_solucao.espacos),
            "Valores = %s\n" % str(ag.melhor_solucao.valores),
            "Cromossomo = %s\n" % str(ag.melhor_solucao.cromossomo),
            "Nota = %s\n" % ag.melhor_solucao.nota_avaliacao)
    
    
    print("\n"*8)
    
    limite = 3
    tamanho_populacao = 2000
    taxa_mutacao = 0.01
    numero_geracoes = 100
    ag = AlgoritmoGenetico(tamanho_populacao)
    resultado = ag.resolver(taxa_mutacao, numero_geracoes, espacos, valores, limite)
    for i in range(len(lista_produtos)):
        if resultado[i] == '1':
            print("Nome: %s R$ %s " % (lista_produtos[i].nome,
                                       lista_produtos[i].valor))
    
    plt.plot(ag.lista_solucoes)
    plt.title("Acompanhamento dos valores")
    plt.savefig("grafico.png")