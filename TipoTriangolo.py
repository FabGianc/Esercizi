""" Applicazione che chiede all'utente di inserire 3 interi 
  	a, b e c da tastiera, li legge e stampa un messaggio 
  	che dice all'utente se il triangolo con lati a, b e c 
  	è equilatero, isoscele o scaleno. """

# INPUT
lato1, lato2, lato3 = input("Caro utente, introduci le lunghezze dei lati di un triangolo: ").split()

lato1 = int(lato1)
lato2 = int(lato2)
lato3 = int(lato3)
	

# OUTPUT 
if(lato1==lato2 and lato1==lato3): 
	print("Il triangolo e' equilatero.")
elif(lato1==lato2 or lato1==lato3 or lato2==lato3): 
	print("Il triangolo e' isoscele.")
else:
	print("Il triangolo e' scaleno.")

