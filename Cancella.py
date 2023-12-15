"""
Definire una funzione cancella(l, i) che data una lista l ed un intero i restituisce una nuova lista (senza modificare l) 
che contiene tutti gli elementi di l eccetto l'elemento in posizione i.
 
Nota: non si può utilizzare la funzione pop.
"""

def cancella(l, i):
    # Inizializzo la nuova_lista che conterrà tutti gli elementi di l tranne quello con indice i
    nuova_lista = []
    # Itero lungo la lista
    for j in range(0, len(l)):
        # Alla nuova_lista aggiungo tutti gli elementi tranne quello con indice i
        if j != i:
            nuova_lista += l[j]
            
    # Restistuisco la nuova_lista
    return nuova_lista

print(cancella([], -1))
print(cancella([], 0))
print(cancella([1], 0))
print(cancella(['a','b','c','d'], -1))
print(cancella(['a','b','c'], 1))
print(cancella(['a','b','c'], 5))