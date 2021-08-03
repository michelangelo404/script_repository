# -*- coding: utf-8 -*-
lista = []
def maxNumeri():
	while True:
		numero = int(input("scrivi un numero: "))
		if numero == 0:
			break
		lista.append(numero)
	pos = lista.index(max(lista))
	print("il massimo tra {} è {} che è stato il numero {} che hai inserito nella lista". format(lista,max(lista),pos))
maxNumeri()
