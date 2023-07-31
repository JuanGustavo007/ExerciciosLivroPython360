"""
A partir da seguinte lista ["C", "Javascript", "Lua", "Python"] verifique primeiramente
e retorne ao usuario se a linguagem python consta na lista, retorne uma mensagem amigavel
ao usuario para estas duas situaçoes.
"""

lista = ["C", "Javascript", "Lua", "Python"]

if lista.__contains__("Python"):
	print("Que top, python está na lista")
else:
	print("Adiciona ai irmao")
