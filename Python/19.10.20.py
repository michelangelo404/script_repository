#giorno 1
#Funzioni con risultati
#posso assegnare una funzione ad una variabile
def scomposizione(c):
	a = c - 2 - 10
	return a
	
    #se volessi un valore stampato a schermo devo
    #inserire 'return' dentro la funzione

#se non inserisco return, la funzione non ritorna valore
#quindi viene stampato 'None'
var = (scomposizione(6))
print(var)

#Prova per stampa di 'None'
def valoreNullo(x):
	y = 13 + x

prova = (valoreNullo(4), "5")
print(prova)    
#ecco infatti che viene stampato solo la string "5"
#e il valore nullo

#Esecuzione condizioninale

a = 16
b = 128


if b > a:
	print("b > a")
else:
	print("tutte le altre condizioni")
	#in if posso mettere else, corrisponde all'italiano
	#"altrimenti" in questo caso verrà stampato b > a

def formulaMagica():
	giuseppe = ("alto")
	anselmo = ("basso")
	if giuseppe == ("alto"):
		print("giuseppe è alto")
	else:
		print("giuseppe è basso")

formulaMagica()
#Sono riuscito a mettere un if dentro una funzione
#ora posso mettere una funzione all'interno della condizione

def funct1():
	nome = ("Claudio")
	claudio = ("ciao" + " " + nome)
	return claudio
	#nota bene che qui per far comparire la frase corretta
	#bisogna inserire il simbolo di addizione
	#si può comodamente cambiare per sapere cosa succede
	#se si inseriscono le virgole
	
if funct1() == ("ciao claudio"):
	print("ho salutato claudio")
else:
	print("output non coincide")
	
print(brasilia())
#ricordarsi gli spazi e i doppi punti!

#esercizio condizioni annidate
def confronta(a, b):
	if a > b:
		print(a + " " + "è maggiore di" + " " + b)
	elif a < b:
		print("a è minore")
	elif a == b:
		print(a + " " + "è uguale a" + " " + b)
	else:
		print("sos")

def elaboraScelta(scelta):
	if scelta > 44:
		print(scelta + " " + "è maggiore di" + " " + 44)
	elif scelta == 33:
		print(scelta + " " + "è uguale a" + "33")
	else:
		print("nessuna corrispondenza")

confronta(2, 12)
elaboraScelta(33)

#Espressioni booleane

a = 16
b = a > 8 and a < 32
#è vero è falso che 'a' è maggiore di 8 e minore di 32?
print(b)

c = 128
z = c == 128

print(z)

a = 0
b = a and 1
print(b)

#vedere pagina 56 4.3 Operatori logici
#cit. ogni valore diverso da zero viene
#considerato vero e lo zero è considerato falso
#in questo caso risulta '0' perchè è falso
a = 2
b = a and 0
print(b)

