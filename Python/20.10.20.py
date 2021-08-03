#Giorno 2

#Istruzione return pagina 60

import math 
import sys

def stampaLogaritmo(x):
	if x <= 0:
		print("Il valore deve essere positivo")
	return

risultato = math.log(5)
print("il risultato è",risultato)
#nota bene che ho messo le virgole perchè così come parametro
#di print può essere accettato anche un valore float

#Ricorsione pagina 60

def contoAllaRovescia(a):
	if a == 0:
		print("Partenza")
	else:
		print(a)
		contoAllaRovescia(a-1)

contoAllaRovescia(2)
"""in questo caso la funzione, dato un parametro a
riduce il parametro fino a 0, in modo che che venga stampato
il numero precedente, fino appunto allo 0, che
corrisponde allo 0

Inserimeto da tastiera

s = input("input: ")
raw_input in python 3 è sostituito da input
ogni volta che devo inserire un valore float o int 
devo perforza convertirlo con float() o int()
perciò si puo provare a inserire un numero e sommarlo
per provare il messaggio d'errore
somma = 3 + s
per risolverlo:
"""
a = input("inserisci numero ")
differenza = int(a) + 44
print(differenza)
#nota bene che int() deve essere usato all'interno
#della variabile, python non lo ricorda se messo prima


#Capitolo 5
#Funzioni produttive, valori di ritorno pag 60
inserimento = input("inserire raggio cerchio: ")
def areaDelCerchio(Raggio):
	temp = math.pi * int(Raggio)**2
	return temp

formula = areaDelCerchio(inserimento) + 5
print(formula)



