"""
Crie duas variaveis com dois valores numericos inteiros digitados
pelo usuario, caso o valor do primeiro numero for maior que o do segundo
exiba em tela uma mensagem de acordo, caso contrario, exiba uma dizendo que o primeiro valor digitado
que o segundo.

"""

valor = int(input("Digite um valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor > valor2:
    print("O primeiro valor digitado é maior")
elif valor2 > valor:
    print("O segundo valor digitado é maior")
else:
    print("Os valores são iguais")
