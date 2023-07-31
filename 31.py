"""

Crie um programa que realiza a progressao aritmetica de 20
elementos, com primeiro termo e razao definidos pelo usuario
"""

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))


valor_inicial = primeiro_termo
k = 0
for i in range(20):
	if i == 0:
		k = valor_inicial
		print(f"Valor inicial {k}")
	k += razao
	print(k)
