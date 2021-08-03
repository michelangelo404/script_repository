#Giorno 3

#Valori di ritorno - continuo
#vediamo cosa succede quando si mettono 2 return
import math

def valoreAssoluto(x):
	if x < 0:
		return - x
	else:
		return x
#se dato un valore x, questa funzione verifica
#se x è minore di 0, in quel caso verrà stampato |x|
#nel caso fosse maggiore di 0, verrà comunque stampato |x|
#proprio perchè ho inserito un return dopo
valoreAssoluto(5)
print(valoreAssoluto(3))

#Formula di topografia

lato1 = input("inserire primo lato: ")
lato2 = input("inserire secondo lato: ")
angolo = input("inserire angolo: ")

def formulaCarnot(lato1, lato2, angolo):
	angolo = math.pi / 200 * float(angolo)     #math.pi non è una funzione richiamabile, quindi non vanno le parentesi coi parametri
	lato1_quadrato = (float(lato1))**2
	lato2_quadrato = (float(lato2))**2
	somma1 = lato1_quadrato + lato2_quadrato
	moltiplicazione1 = 2 * (float(lato1)) * (float(lato2))
	moltiplicazione_cos = moltiplicazione1 * math.cos(float(angolo))
	ris_parziale = somma1 - moltiplicazione_cos
	ris_finale = math.sqrt(float(ris_parziale))
	print(angolo, lato1_quadrato, lato2_quadrato, somma1, moltiplicazione1, moltiplicazione_cos, ris_parziale)
	return ris_finale

print(formulaCarnot(lato1, lato2, angolo))

print((float(lato2))**2)


