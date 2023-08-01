"""
Crie uma funcao que pode conter dois ou mais parametros, porem sem um numero definido e declarado
de parametros
"""


def funcao_varios_nomes(arg1, *args):
	return f"Boa noite professor {arg1} e {args}"


print(funcao_varios_nomes("Juan", "Gustavo", "Pedro"))
