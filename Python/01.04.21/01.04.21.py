from datetime import datetime as dt
from datetime import date 
def creazioneFile():
	global f 
	data = dt.now()
	to_str = dt.isoformat(data)
	cutter = to_str[:10]
	f = open(cutter, "a")

def contenuto():
	richiesta = input("dimmi cosa scrivere per il diario di oggi: ")
	f.write(richiesta)
creazioneFile()
contenuto()
