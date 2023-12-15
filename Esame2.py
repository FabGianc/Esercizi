"""
Scrivere un programma che, data una lista di interi non nulli Lista con almeno due elementi, 
memorizzi in una variabile Booleana Risultato il valore True se la lista è costituita 
da un sequenza alternata di valori positivi e negativi, False altrimenti.
Attenzione: il primo valore può essere sia positivo che negativo.
Per esempio, con Lista=[-1,3,-5,9] e con Lista=[1,-3,5,-9], la variabile Risultato dovrà  
contenere il valore True al termine dell'esecuzione del programma. 
Mentre, con Lista=[1,3,-5,9], la variabile Risultato dovrà contenere il valore False 
al termine dell'esecuzione del programma.  

Nota: 

    Non è consentito l'uso di istruzioni print e input diverse da quelle già presenti.
    Non è consentita l'inclusione di librerie.
    Non è consentita la definizione di funzioni.

"""

# Inizializza la lista di interi
# Inizializza la lista di interi
# Lista = [-1, 3, -5, 9]
# Lista = [-2,32,-23,1,12]
# Lista = [[-34,45,-92,12]]
Lista = [23,12,-3,-45]

# Inizializzo la variabile Risultato
Risultato = True

# Verifico se la lista è costituita da una sequenza alternata di valori positivi e negativi
# Itero da i fino alla lunghezza della lista, con i che parte da 1 perchè devo confrontare
# coppie di elementi
for i in range(1, len(Lista)):
    # Verifico se la sequenza è alternata
    if (Lista[i] >= 0 and Lista[i - 1] >= 0) or (Lista[i] < 0 and Lista[i - 1] < 0):
        Risultato = False

# Stampa il risultato
print("La lista è costituita da una sequenza alternata di valori positivi e negativi:", Risultato)

# Inizializza la variabile Risultato
Risultato = True

# Verifica se la lista è costituita da una sequenza alternata di valori positivi e negativi
i = 1
while i < len(Lista):
    # Verifica se la sequenza è alternata
    if (Lista[i] >= 0 and Lista[i - 1] >= 0) or (Lista[i] < 0 and Lista[i - 1] < 0):
        Risultato = False
    i += 1

# Stampa il risultato
print("La lista è costituita da una sequenza alternata di valori positivi e negativi:", Risultato)
