"""
Crie uma funcao com tres parametros, sendo dois deles com dados/valores padrao
, alterando o terceiro deles contornando o paradigma da justaposicao de argumentos
"""


def funcao_tres_parametros(parametro1=0, parametro2=2, param3=0):
	return f"Os parametros são {parametro1} {parametro2} {param3}"


print(funcao_tres_parametros(10, 0, param3=10))
