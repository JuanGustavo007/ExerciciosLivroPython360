""""
Peça que o usuário digite um numero, em seguida o converta para float
exibindo em tela tanto o numero em si quanto o seu tipo de dado
"""

valor_entrada = int(input("Digite um valor"))
valor_convertido = float(valor_entrada)
print(f"Antes da conversão {valor_entrada}" + f"e o seu tipo de dado {type(valor_entrada)}")
print(f"Depois da conversão {valor_convertido}" + f"e o seu tipo de dado {type(valor_convertido)}")

