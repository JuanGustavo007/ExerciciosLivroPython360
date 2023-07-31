"""
Crie um programa que pede ao usuario que o mesmo digite um
numero qualquer, em seguida retorne se esse numero é primo ou nao,
caso, nao retorne tambem quantas vezes esse numero e divisivel
"""

numero = int(input("Digite um numero: "))
divisoes = 0

for i in range(1, numero + 1):
	if numero % 1 == 0:
		divisoes +=1

if divisoes == 2:
	print(f" {numero} é primo!!")
	print(f"{numero} é divisivel por 1 ou por {numero}")
else:
	print(f"{numero} nao é primo")
	print(f"{numero} é divisivel {divisoes} vezes")