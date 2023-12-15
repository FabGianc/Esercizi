"""
Scrivere un programma che, data una lista di interi non nulli Lista con almeno due elementi, 
memorizzi in una variabile Booleana Risultato il valore True se la lista è costituita 
da un sequenza alternata di valori positivi e negativi, False altrimenti.

Attenzione: il primo valore può essere sia positivo che negativo.
Per esempio, con Lista=[-1,3,-5,9] e con Lista=[1,-3,5,-9], la variabile Risultato dovrà  
contenere il valore True al termine dell'esecuzione del programma. Mentre, 
con Lista=[1,3,-5,9], la variabile Risultato dovrà contenere il valore False al termine 
dell'esecuzione del programma.  
"""


# Inizializza la lista di interi
Lista = [-1, 3, -5, 9]

# Inizializza la variabile Risultato
Risultato = True

# Verifica se la lista è costituita da una sequenza alternata di valori positivi e negativi
for i in range(1, len(Lista)):
    # Verifica se la sequenza è alternata
    if (Lista[i] >= 0 and Lista[i - 1] >= 0) or (Lista[i] < 0 and Lista[i - 1] < 0):
        Risultato = False
        break

# Stampa il risultato
print("La lista è costituita da una sequenza alternata di valori positivi e negativi:", Risultato)
