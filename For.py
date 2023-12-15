"""
Esempi di utilizzo dell'istruzione ripetitiva for
"""

a , b = input("Inserisci due interi positivi separati da uno spazio: ").split()

a = int(a)
b = int(b)

if a < b:
    for i in range(a,b):
        print(i)
else:
    for i in range(a,b, -1):
        print(i)