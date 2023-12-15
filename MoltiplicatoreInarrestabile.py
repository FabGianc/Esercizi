"""
Esercizio 006
Moltiplicatore Inarrestabile

Scrivi un programma "moltiplicatore" che, data una lista di numeri, moltiplichi tra loro tutti gli elementi.
"""

# Creo la lista Numeri
Numeri = [2, 4, 6, 1, 7, 14]

# Inizializzo la variabile moltiplicatore al valore neutro 1
moltiplicatore = 1

for num in Numeri:
    moltiplicatore *= num

print("Il prodotto di tutti gli elementi è: ",moltiplicatore)