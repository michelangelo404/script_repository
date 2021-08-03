#Giorno 13
#porto l'esercizio di C su python

def numeroMassimo(n):
	k = 0
	somma = 0
	while somma < n:
		k += 1
		k1 = k + 1
		somma = k + k1
		print(somma)
		print("il numero massimo è ", k)

numeroMassimo(45)

n = int(input("inserire numero positivo"))
i = 1
somma = 0
while somma < n:
	i += 1
	somma = somma + i
k = i - 1

print("il k massimo della somma di k minore di n è: ", k)

def prima(parola):
	return parola[0]
def ultima(parola):
	return parola[-1]
def mezzo(parola):
	return parola[1:-1]

print(mezzo("er"))

