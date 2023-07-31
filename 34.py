"""
Crie um programa que realiza a contagem de 1 ate 100
usando apenas numeros impares, ao final do processo
exiba em tela quantos numeros impares foram encontrados
nesse intervalo, assim como a soma dos mesmos
"""
soma = []
for i in range(101):
	if i % 2 != 0:
		soma.append(i)
		print(i)
		

print(f"O total de numeros impares é {len(soma)} e a sua soma é de {sum(soma)}")

