"""
Crie um programa que le um valor de inicio e valor de fim,
exibindo em tela a contagem dos numeros dentro desse intervalo
"""
valor_inicio = int(input("Digite um valor: "))
valor_fim = int(input("Digite um valor de fim: "))
diferenca = valor_fim - valor_inicio

for i in range(valor_fim):
	if i > valor_inicio:
		print(i)
	else:
		print("vish")