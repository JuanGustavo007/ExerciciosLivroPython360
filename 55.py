"""
Crie uma funcao que recebe um nome como parametro e exibe em tela uma mensagem
de boas-vindas.O nome deve ser fornecido pelo usuario, incorporado na mensagem
de boas-vindas da funcao
"""
input_user = input("Diga-me seu nome primeiramente? ")


def funcao_boas_vindas(pessoa):
	print(f"Boas-vindas {pessoa}")


funcao_boas_vindas(input_user)
