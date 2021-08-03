#Giorno 10

def fahrenheitCelsius(grado_celsius, grado_fahrenheit):
	conversione_fahrenheit = (grado_celsius * 9 / 5) + 32#(32 °C × 9/5) + 32 = 89,6 °F
	conversione_celsius = (grado_fahrenheit - 32) * 5 / 9
	print(conversione_fahrenheit)
	print(conversione_celsius)
	
fahrenheitCelsius(23, 45)
