#script per impostare una parola per riga in un file di testo

with open("test.txt", "r") as f, open("test_edit.txt", "w") as f1:
	for riga in f:
		f1.write("\n".join(riga.split()))
		f1.write("\n")

#l'istruzione with viene usata sopratutto con i file, with fa in modo che
#il file venga chiuso automaticamente
