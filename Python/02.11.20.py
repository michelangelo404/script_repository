#Giorno 15

def numeroPrimo(x):
	conta = 0
	div = 1
	while conta <= 1 and div <= x/2:
		if x%div == 0:
			conta = conta + 1
		div = div + 1
	if conta == 1:
		return "è un numero primo"
	else:
		return "non è un numero primo"
print(numeroPrimo(2))
