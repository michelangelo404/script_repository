# -*- coding: utf-8 -*-
fattoria = 0
abitanti = 2
legno = 200
argilla = 140
oro = 100
def fattoriaLivUno():
	global fattoria
	global abitanti
	fattoria = (fattoria + 1)
	abitanti = (abitanti + 2)
def scelta():
	sceltaInput = input("Vuoi aumentare il livello della tua fattoria? digita si oppure no, per visualizzare le statistiche digita ?") 
	if sceltaInput == ("si"):
		config = open("dati.txt", "w")
		config.write(sceltaInput)
		fattoriaLivUno()
	elif sceltaInput == ("no"):
		print("il livello non sarà aumentato")
#	elif scelta == ("?"):
#		statistiche()
	else:
		print("no corrispondenza")
		scelta() #Errore corretto: qui ho chiamato la funzione "scelta" che coincideva con il nome della variabile soprastante "scelta", in questo modo compariva l'errore "str in not callable" proprio perchè python individuava scelta() come la variabile "scelta"(ora cambiata in sceltaInput)
scelta()
#def fattoriaLivDue():
	
