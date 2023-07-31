"""
A partir de um simpes dicionario composto por tres itens ["Alto nivel": 'Python', "Medio nivel": 'c',
'Baixo nivel': 'Assembly'] verifique se 'python' consta no dicionario em questao, utilizando negacao logica
para tal verificacao
"""
linguagens = {"Alto nivel": 'Python', "Medio nivel": "C", "Baixo nivel": 'Assembly'}
valores_lin = linguagens.values()

for i in valores_lin:
	if i == "Python":
		print("Consta na lista")
		
