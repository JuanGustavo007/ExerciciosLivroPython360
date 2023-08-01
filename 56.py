"""
Crie uma funcao que recebe um valor digitado pelo usuario
e eleva esse valor ao quadrado
"""

input_user = int(input("Diga-me um valor? "))


def funcao_quadrado(valor):
	return valor ** 2


print(f"O valor elevado ao quadrado é de {funcao_quadrado(input_user )} ")
