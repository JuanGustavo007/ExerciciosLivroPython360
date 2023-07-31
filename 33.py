"""
Crie um programa que faz a contagem regressiva de 20 segundos
"""
import time

segundos = 20


def retirar_tempo(segundos):
	for i in range(segundos):
		time.sleep(3)
		segundos = segundos - 1
		print(segundos)


retirar_tempo(segundos)
