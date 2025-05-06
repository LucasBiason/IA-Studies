# Meu Investimento

Uma biblioteca Python para cálculos de investimentos.

## Instalação

Você pode instalar a biblioteca via pip:

```bash
pip install meu_investimento
```

## Uso

```python
from investimentos import calcular_retorno_investimento, calcular_juros_compostos

valor_inicial = 1000
valor_final = 1500

retorno = calcular_retorno_investimento(valor_inicial, valor_final)
print(f"Retorno do investimento: {retorno:.2f}%")

valor_final_juros = calcular_juros_compostos(valor_inicial, 6, 5)
print(f"Valor final com juros compostos: R${valor_final_juros:.2f}")
```