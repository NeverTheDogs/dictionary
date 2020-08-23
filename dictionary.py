#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os, string
os.system('clear')

####### COLORS
class col:
    PINK = '\033[95m'
    PURPLE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'    
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

######## START FUNCTION

def reader():
	print col.YELLOW
	a=raw_input("Nome del file con le parole -->	"+col.END)
	with open(a,'r') as f:
		for riga in f:
			riga = riga.rstrip('\n')
			list.append(riga)

def create3():
	a=len(list)
	b=len(special)
	#print col.YELLOW+"Creazione combinazioni triple"+col.END
	with open('word.txt','a+t') as f:
		for x in xrange(0, a):
			for y in xrange(0,a):
				for z in xrange(0,a):
					for s in xrange(0,b):
						if (list[x]==list[y]) or (list[x]==list[z]) or (list[z]==list[y]):
							continue
						else:
							f.write(special[s]+list[x]+list[y]+list[z]+'\n')
							f.write(list[x]+special[s]+list[y]+list[z]+'\n')
							f.write(list[x]+list[y]+special[s]+list[z]+'\n')
							f.write(list[x]+list[y]+list[z]+special[s]+'\n')
	f.close()
	#print col.PINK+"Il file word.txt è stato salvato nella cartella contenente l'eseguibile"+col.END

def create2():
	a=len(list)
	b=len(special)
	print 
	print col.YELLOW+"Il dizionario creato verra salvato come 'word.txt'"+col.END
	if a==0:
		print col.RED+"La lista è ancora vuota"+col.END
	else:
		if os.path.isfile('word.txt'):
			print 
			print col.RED+"Esiste già un file con questo nome modificalo oppure verrà sovrascritto"+col.END
		else:
			print
			print col.YELLOW+"Creazione dizionario in corso..."+col.END
			with open('word.txt','w+t') as f:
				for x in xrange(0, a):
					for y in xrange(0,a):
						for s in xrange(0,b):
							if list[x]==list[y]:
								continue
							else:
								f.write(list[x]+list[y]+'\n')
								f.write(special[s]+list[x]+list[y]+'\n')
								f.write(list[x]+special[s]+list[y]+'\n')
								f.write(list[x]+list[y]+special[s]+'\n')
			f.close()
			print
			print col.PINK+"Il file word.txt è stato salvato nella cartella contenente l'eseguibile"+col.END

def rem():
	print col.YELLOW
	a=raw_input("Inserici l'elemento da cancellare -->	"+col.END)
	b=a in list
	if b==1:
		c=list.index(a)
		del list[c]
		print
		print col.PINK+"Parola eliminata!"
	else:
		print
		print col.RED+"La parola non è presente nella lista"+col.END

def word(n):
	print
	print col.YELLOW+"Inserici le parole qui a seguire"+col.END
	try:
		for i in range(1,n):
			print
			x=raw_input("-->:  ")
			if x in list:
				print "La parola è già stata inserita!"
				continue
			elif x=="":				
				print "Non è stata inserita nessuna parola"
				continue
			else:
				list.append(x)
				print
	except (KeyboardInterrupt, EOFError):
		print
		print col.PINK+"Fine inserimento parole!"

def menu():
	print
	print col.PURPLE+"	1) "+col.END+"Inserisci nuove parole;"
	print col.PURPLE+"	2) "+col.END+"Rimuovi parole;"
	print col.PURPLE+"	3) "+col.END+"Stampa lista;"
	print col.PURPLE+"	4) "+col.END+"Carica dizionario esistente;"
	print col.PURPLE+"	5) "+col.END+"Crea combinazioni;"
	print
	print
	c=input("Fai la tua scelta: ")
	if c==1:
		word(n);
	elif c==2:
		rem();
	elif c==3:
		os.system("clear")	
		print
		print col.GREEN+"	Lista di parole inserite"
		print
		if len(list)==0:
			print col.RED+"La lista è ancora vuota"+col.END
		else:
			print list
			print col.END
	elif c==4:
		reader();
	elif c==5:
		a=len(list)
		if a<=1:
			print col.RED+"La lista non ha sufficienti elementi"+col.END
		elif a==2:
			create2();
		else:
			create2();
			create3();
	else:
		menu();

###### START MAIN
n=9999
list = []
special =["@", "/", "&", "%", "_", "-", ".", "?", "€", "$"]
print
print col.GREEN+"	Dizionario per malati"
print "-----------------------------------------------------------"+col.END
print "Inserisci delle parole e verrano create combinazioni"
print col.END
while True:
	try:
		menu();
	except (NameError, SyntaxError):
		print
		print
		print col.RED+"Errore"+col.END
	except (KeyboardInterrupt, EOFError):
		print
		print
		print col.RED+"ctrl+z per mettere fine al programma"+col.END
	





