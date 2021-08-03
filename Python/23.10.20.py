#Giorno 5

#Tabelle bidimensionali

i = 1
while i <= 6:
	print (2*i," ",)
	i = i + 1

#Capitolo 7
#Stringhe

Saluto = "ciao"
Lettera = Saluto[1]
print(Lettera)
#in questo caso stampo la variabile 'Lettera'
#che dice di prendere la prima lettera del dato della variabile 'Saluto'
#attenzione che non dice di prendere la prima lettera di saluto
#e se scrivessi ciao[1] mi darebbe un errore dicendo che 'ciao' non è definita

frutto = "avocado"
print(len(frutto))
'''
mi stamperà la lunghezza della parola
ora voglio vedere se riesco a stampare la lettera usando la variabile
lunghezza = len(frutto)
lettera_frutto = frutto[lunghezza]
mi da' errore poiché le arrays startano da 0, in questo caso quindi 6, non c'è
dovrò fare sempre così
'''
lunghezza = len(frutto)
ultima_l = frutto[lunghezza - 1]
print(ultima_l)

#Ciclo for

Indice = -1
c = 0
while c < len(frutto):
	Lettera = frutto[Indice]
	print( Lettera )
	Indice = Indice - 1
	c = c + 1

for Lettera in frutto:
	print(Lettera)
#funziona lo stesso anche se 'Lettera' conserva come dato
#la seconda lettera di ciao

Prefissi = "JKLMNOPQ"
Suffisso = "ack"

for Lettera in Prefissi:
	print(Lettera + Suffisso)
