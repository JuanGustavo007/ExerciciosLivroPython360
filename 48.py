"""
Crie uma simples estrutura de dados simulando um cadastro de uma loja.
Nesse cadastro deve conter informacoes como nome, idade, sexo, estavo civil,
nacionalidade, faixa de renda... exiba tais dados
"""


class Funcionario:
	def __init__(self, nome, idade, sexo, estavo_civil, nacionalidade, faixa_renda):
		self.nome = nome,
		self.idade = idade,
		self.sexo = sexo,
		self.estado_civil = estavo_civil,
		self.nacionalidade = nacionalidade,
		self.faixa_renda = faixa_renda


novo_funcionario = Funcionario("juan", 20, "M", "Solteiro", "Brasileira", 2000)
print(novo_funcionario.idade)
