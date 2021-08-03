#Giorno 4
#Ancora ricorsione pag. 72

import math
def fattoriale(n):
	if n == 0:
		return 1
	else:
		FattorialeMenoUno = fattoriale(n-1)
		Risultato = n * FattorialeMenoUno
		return Risultato
		
print(fattoriale(5))
#ricordarsi diagramma di stack a pagina 73

#Controllo dei tipi pag. 57

input_utente = float(input("Digita un valore con la virgola: "))

def nuovaFormula(input_utente):
	if type(input_utente) != type(1.4):
		print("Non è un valore corretto!")
	else:
		print("Calcolo... ")

nuovaFormula(input_utente)

#Assegnazione e confronto pag.77

numero = 5
print(numero)
numero = 4
print(numero)

a = 3
b = a
#in questo caso 'b' prende il valore attuale di a cioè 3
a = 7 
#ora a e b sono diversi in quanto a vale 7, ma b vale comunque 3

#Istruzione while

def ContoAllaRovescia(n):
	while n > 0:
		print (n)
		n = n-1
	print ("Partenza!")
#quando la condizione è accettata, ovvero "finché" n è maggiore di 0
#verrà stampato n, quando il while, non è soddisfatto, si interrompe e
#quindi si passa a print
#print(ContoAllaRovescia(99))

def potenzeDiDue(x):
	while x < 65536.0:
		print (x, '\t', math.log(x)/math.log (2.0))
		x = x * 2.0
potenzeDiDue(2)

print("ciao", "\n", "\t", "come", "\n", "\t", "\t", "stai")
