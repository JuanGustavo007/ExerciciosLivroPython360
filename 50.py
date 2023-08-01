"""
Crie um sistemas de perguntas e respostas que interage
com o usuario, pedindo que o mesmo insira uma resposta.
Caso a primeira questao esteja correta, exiba em tela uma mensagem de acerto
e parta para a proxima pergunta, caso incorreta, exiba uma mensagem de erro
e pule para a proxima pergunta
"""

perguntas = ["Qual dia é hoje?", "Qual a data do seu aniversário?", "Qual dia da semana é hoje?"]
respostas = ["31/07/2023", "01/02/1998", "Segunda-feira"]

for i in range(len(perguntas)):
	input_user = input(perguntas[i])
	if input_user == respostas[i]:
		print("Resposta correta!!!")
	else:
		print("Tente acertar na próxima questão!!!")
