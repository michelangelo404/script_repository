#Giorno 6

prefissi = "JKLMONPQ"
suffisso = "ack"
suff_corretto = "uack"

for Lettera in prefissi:
	print(Lettera + suffisso)

for Lettera in prefissi:
		if Lettera == 'O' or Lettera == 'Q':
			print(Lettera + suff_corretto)
		else:
			print(Lettera + suffisso)

#Slicing
#una parte di testo è chiamato 'slice'

s = 'Monty Python'
print(s[0:5])
#stampa le lettera da 0 a 5
#il ':' è inteso come 'da a' è quindi l'indicatore di intervallo
print(s[6:12])

frutto = 'banana'
print(frutto[:3])
#se non è definito l'inizio, stamperà fino al carattere numero 3
print(frutto[3:])
#se non è definito l'ultimo carattere, stampa tutto dal 3 fino alla fine
print(frutto[:])
#in questo caso stamperà tutto, anche se non c'è alcun indice

saluto = 'Ciao, mondo!'
nuovo_saluto = 'Ragazzi' + saluto[1:]
print(nuovo_saluto)

def trova(parola, lettera, inizio):
	indice = inizio
	while indice < len(parola):
		if parola[indice] == lettera:
			return indice
		indice = indice + 1
	return "Lettera non trovata"
	
print(trova("ciao ragazzi", "r", 4))

def contatoreLettere(parola, carattere, inizio):
	indice = 0
	conta = 0
	while True:
		indice = trova(parola, carattere, inizio)
		for lettera in parola:
			if lettera == carattere:
				conta = conta + 1
		return conta

print(contatoreLettere("ciao come stai", "a", 8))
#da mettere a posto

