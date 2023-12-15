"""
Scrivere un frammento di codice che, dati due numeri naturali b e h, visualizza un
rettangolo di asterischi di base b e altezza h
"""

b = int(input("Inserisci un valore intero per la base del rettangolo: "))
h = int(input("... e uno per l'altezza: "))

for j in range (h):
    for i in range (b):
        print("*", end='')
    print()