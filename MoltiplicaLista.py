"""
Scrivere un programma Python che contiene una funzione
moltiplicaLista che prende in input una lista di valori numerici e
restituisce il prodotto di tutti i valori della lista. La funzione ha un
parametro Booleano opzionale risultatoIntero, il cui defult è False, che -
se True - richiede che il risultato sia approssimato al suo valore intero.
"""

def moltiplicaLista(L, risultatoIntero = False):
    prodotto = L[0]
    risultato = 0
    for i in range(1, len(L)):
        prodotto *= L[i]
    
    if risultatoIntero:
        risultato = int(prodotto)
    else:
        risultato = prodotto
    return risultato


Lista = [12, 13, -8, 9, 1.2, 3]
print(moltiplicaLista(Lista))
print(moltiplicaLista(Lista, True))