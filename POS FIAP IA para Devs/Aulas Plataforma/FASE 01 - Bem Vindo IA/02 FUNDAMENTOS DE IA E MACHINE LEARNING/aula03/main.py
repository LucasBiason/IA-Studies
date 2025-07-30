# main.py

import investimentos

valor_inicial = 1000
valor_final = 1500
anos = 5
taxa_anual = 6

retorno = investimentos.calcular_retorno_investimento(valor_inicial, valor_final)
print(f"Retorno do investimento: {retorno:.2f}%")

valor_final_juros = investimentos.calcular_juros_compostos(valor_inicial, taxa_anual, anos)
print(f"Valor final com juros compostos: R${valor_final_juros:.2f}")

taxa_mensal = investimentos.converter_taxa_anual_para_mensal(taxa_anual)
print(f"Taxa de juros mensal: {taxa_mensal:.2f}%")

cagr = investimentos.calcular_cagr(valor_inicial, valor_final, anos)
print(f"CAGR: {cagr:.2f}%")