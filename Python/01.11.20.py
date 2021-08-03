#Giorno 14

#Esercizi capitolo 6.11 pag.61

def prima(parola):
	return parola[0]
def ultima(parola):
	return parola[-1]
def mezzo(parola):
	return parola[1:-1]


def palindromo(parola):
	lunghezza = len(parola)
	parola_mezzo = parola[1:-1]
	if len(parola) >= 3 :
		if prima(parola) == ultima(parola) and palindromo(parola_mezzo):
			return True
		else:
			print(parola, " non è un palindromo")
	else:
		return True
print(palindromo("ciao"))

#Un numero, a , è una potenza di b se è divisibile per b e a/b è a sua volta una potenza
#di b . Scrivete una funzione di nome potenza che prenda come parametri a e b e che restituisca True
#se a è una potenza di b . Nota: dovete pensare bene al caso base.

def potenza(a, b):
	divisione_ab = a % b
	divisione_a_ab = a % (a/b)
	print(divisione_ab)
	print(divisione_a_ab)
	if divisione_ab == 0 and divisione_a_ab == 0.0:
		return True
	else:
		return "a non è potenza di b"

print(potenza(144, 13))

def mcd(a, b):
	if a > b:
		divisione_r = a % b
		if divisione_r == 0.0:
			print("l'mcd è ", b)
		elif divisione_r != 0.0:
			return mcd(b, divisione_r)
		else:
			return "l'mcd è 1"
	else:
		return "a deve essere maggiore di b"
print(mcd(125456, 400))

