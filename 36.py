"""
Crie um programa que pede que o usuario digite um nome ou frase
verifique se esse conteudo digitado é um palidromo ou nao,
exibindo em tela o resultado
"""

nome = "juan"

for i in range(len(nome)):
	if nome[i] == nome[-i]:
		print(nome[-i])