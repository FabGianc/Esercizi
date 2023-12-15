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

Lista = [11, -12., 1, -1, 3]

Risultato = all([Lista[i]*Lista[i+1]<0 for i in range(0,len(Lista)-1)])

print(Risultato)
