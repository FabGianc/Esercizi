"""
Definire una funzione somma_interi(l) che data una lista di interi l ne restituisce la somma.
"""

def somma_interi(l):
    # Inizializzo la variabile somma al valore neutro 0
    somma = 0

    # Ciclo per tutti gli elementi della lista
    for i in range(0, len(l)):
        # Aggiunngo a somma il valore dell'elemento i-esimo
        somma += l[i]
        
    # Restitisco la somma di tutti gli elementi
    return somma

print(somma_interi([-3,-2]))