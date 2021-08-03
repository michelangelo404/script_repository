#Giorno 7

import math
import random
raggio = input("raggio: ")

pi = math.pi
area_cerchio = pi * int(raggio)**2
print(area_cerchio)

prodotto = input("prezzo da scontare: ")
sconto = input("sconto(senza percentuale): ")

prezzo_scontato = int(prodotto) * int(sconto) / 100
print(prezzo_scontato)

N = int(input("Numero massimo da generare: "))

for i in range(10):
	x = random.randrange(0,N)
	print(f", {x}",end="") 
#f serve per la formattazione delle stringhe
