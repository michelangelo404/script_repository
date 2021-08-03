#Giorno 9

parola = input("Scrivi una lettera dell'alfabeto: ")

if parola == "a" and "e" and "i" and "o" and "u":
	print("è una vocale")
else:
	print("non è una vocale")

def tabellinaNumero(x):
	i = 1
	while i <= 10:
		if x > 0:
			print(x, " X ", i, " =", x*i)
		else:
			return ("sos")
		i = i + 1

print(tabellinaNumero(23))
numero = input("dammi un numero")

