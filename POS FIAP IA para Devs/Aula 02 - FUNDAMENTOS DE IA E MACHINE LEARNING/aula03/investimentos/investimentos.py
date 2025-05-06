# investimentos.py

def calcular_retorno_investimento(valor_inicial, valor_final):
   """
   Calcula o retorno de investimento.

   Args:
       valor_inicial (float): Valor inicial do investimento.
       valor_final (float): Valor final do investimento.

   Returns:
       float: Retorno do investimento em porcentagem.
   """
   retorno = (valor_final - valor_inicial) / valor_inicial * 100
   return retorno

def calcular_juros_compostos(principal, taxa_juros_anual, periodos):
   """
   Calcula o valor final de um investimento com juros compostos.

   Args:
       principal (float): Valor inicial investido.
       taxa_juros_anual (float): Taxa de juros anual em porcentagem.
       periodos (int): Número de períodos (anos).

   Returns:
       float: Valor final após o período com juros compostos.
   """
   taxa_juros_decimal = taxa_juros_anual / 100
   valor_final = principal * (1 + taxa_juros_decimal) ** periodos
   return valor_final

def converter_taxa_anual_para_mensal(taxa_anual):
   """
   Converte uma taxa de juros anual para mensal.

   Args:
       taxa_anual (float): Taxa de juros anual em porcentagem.

   Returns:
       float: Taxa de juros mensal em porcentagem.
   """
   taxa_mensal = (1 + taxa_anual / 100) ** (1 / 12) - 1
   return taxa_mensal * 100

def calcular_cagr(valor_inicial, valor_final, anos):
   """
   Calcula a taxa de crescimento anual composta (CAGR).

   Args:
       valor_inicial (float): Valor inicial do investimento.
       valor_final (float): Valor final do investimento.
       anos (int): Número de anos.

   Returns:
       float: CAGR em porcentagem.
   """
   cagr = ((valor_final / valor_inicial) ** (1 / anos) - 1) * 100
   return cagr