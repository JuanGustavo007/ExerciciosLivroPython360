"""
Crie um programa que recebe dados de um aluno como nome
e suas notas em supostos 3 trimestres de aula, retornando
um novo dicionario com o nome do aluno e a media de duas notas
"""

dicionario_aluno = dict(nome="Juan", trim1=[10, 8, 6, 8], trim2=[10, 8, 6, 8], trim3=[10, 8, 6, 8])
novo_dicionario = dict(nome="Juan", notas=dicionario_aluno["trim1"] +
										  dicionario_aluno["trim2"] + dicionario_aluno["trim3"], media = sum(dicionario_aluno["trim1"] + dicionario_aluno["trim2"] + dicionario_aluno["trim3"]) / len(dicionario_aluno["trim1"] + dicionario_aluno["trim2"] + dicionario_aluno["trim3"]))
print(novo_dicionario)
