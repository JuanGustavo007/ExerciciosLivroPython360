"""
Peca para que o usuario digite um numero, em seguida exiba em tela uma mensagem dizendo se tal numero é
par ou impar
"""


input_user = int(input("Digite um valor: "))

if input_user % 2 == 0:
    print("Valor par")
else:
    print("Valor impar")

