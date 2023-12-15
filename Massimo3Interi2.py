# INPUT 
x, y, z = input("Introduci tre interi: ").split() # variabili per memorizzare tre interi
x = int(x)
y = int(y)
z = int(z)
	
# CALCOLA IL MASSIMO
if(x>y): 
	if(x>z):
		massimo = x
	else:
		massimo = z
elif(y>z):
	massimo = y
else: 
	massimo = z
		
# OUTPUT 
print(f"Il massimo valore e' {massimo}.")


