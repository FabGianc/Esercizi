# INPUT 
x, y, z = input("Introduci tre interi: ").split() # variabili per memorizzare tre interi
x = int(x)
y = int(y)
z = int(z)
	
# CALCOLA IL MASSIMO

massimo = x
	
if(y>massimo):
	massimo = y   # adesso massimo è il massimo fra x ed y

if(z>massimo):
	massimo = z
		
# OUTPUT 
print(f"Il massimo valore e' {massimo}.")

