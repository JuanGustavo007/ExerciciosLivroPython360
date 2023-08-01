"""
Crie uma funcao com dois parametros relacionados ao nome e sobrenome de uma pessoa
a funcao deve retornar uma mensagem de boas-vindas e esses dados devem ser digitados
pelo usuario
"""

input_nome = input("Diga-me seu nome? ")
input_sobrenome = input("Diga-me seu sobrenome? ")


def nome_completo(nome: str, sobrenome: str):
	return f"Boas vindas {nome} {sobrenome}"


print(nome_completo(input_nome, input_sobrenome))
