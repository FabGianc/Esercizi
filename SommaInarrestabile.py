"""
Esercizio 005
Somma Inarrestabile

Scrivi un semplice programma che, data una lista di numeri, sommi tra loro tutti gli elementi.

Suggerimento: anche se esiste la funzione sum() per risolvere l'esercizio potresti usare il ciclo for.
"""

# Creo la lista Numeri
Numeri = [2, 4, 6, 1, 7, 0, -2, 14]

# Inizializzo la variabile somma
somma = 0

for num in Numeri:
    somma += num

print("La somma è: ",somma)