"""
Crie um programa que exibe em tela a tabuada de um determinado numero fornecido
pelo usuario
"""

input_user = int(input("Digite um valor: "))

for i in range(11):
	print(f"{input_user } x {i} = {input_user * i}")
