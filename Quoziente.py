"""
Calcolo del quoziente mediante istruzione ripetitiva while
"""

# Leggo i due valori a e b
a, b = input("Insersci due valori separati da uno spazio: ").split()

a = int(a)
b = int(b)

# Inizializzo il quoziente a 0
q = 0
# Ciclo finché a è maggiore di b
while (a>=b):
    a = a - b
    q +=1

print("Il resto è: ", a)
print("Il quoziente è: ", q)