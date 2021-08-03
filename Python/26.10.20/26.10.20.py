#Giorno 8

parola_20 = "questa è una stringa da venti caratteri"
testo = open("file_testo.txt")
for riga in testo:
	parola = riga.strip()
	if len(parola) > len(parola_20):
		print(parola)
