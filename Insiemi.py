"""
Scrivere un programma Python che contiene:
• una funzione listaIntersezione che prese in input due liste L1 e L2 senza
ripetizioni restituisca una nuova lista che contiene gli elementi comuni a L1 e L2.
• una funzione listaUnione che prese in input due liste L1 e L2 senza ripetizioni
restituisca una nuova lista che contiene gli elementi presenti in L1 o L2.
• una funzione Jaccard che prese in input due liste L1 e L2 senza ripetizioni
restituisce l’indice di jaccard, ovvero, il rapporto tra la dimensione
dell’intersezione di L1 e L2 e la dimensione dell’unione di L1 e L2.
"""

# listaIntersezione legge gli elementi della prima lista e verifica se presente
# nella seconda lista, in caso positivo lo aggiunge nella nuova lista
def listaIntersezione(L1, L2):
    # Inizializzo la lista che conterrà gli elementi comuni
    listaInt = []
    # Itero lungo gli elementi della lista L1 e verifico se è presente in L2 ...
    for i in range(0, len(L1)):
        if L1[i] in L2:
            # ... in caso positivo, aggiungo alla nuova lista
            listaInt.append(L1[i])
    # Restituisco la nuova lista
    return listaInt

# listaUnione legge gli elementi della prima lista e verifica se NON è presente
# nella seconda, se NON è presente lo aggiunge alla nuova lista
# e viceversa, verifica gli elementi della lista L2 che NON siano presenti nella prima
def listaUnione(L1, L2):
    # Inizializzo la lista che conterrà gli elementi NON comuni
    listaU = []
    # Itero lungo gli elementi della lista L1 e verifico se NON è presente in L2 ...
    for i in range(0, len(L1)):
        if L1[i] not in L2:
            # ... aggiungo l'elemento NON presente
            listaU.append(L1[i])
    
    # Ripeto la verifica con ciascun elemento dei L2 con L1 
    for i in range(0, len(L2)):
        if L2[i] not in L1:
            listaU.append(L2[i])
    return listaU

def Jaccard(L1, L2):
    ind_jaccard = len(listaIntersezione(L1, L2)) / len(listaUnione(L1, L2))
    return ind_jaccard


L1 = ["problema", "esempio", "comune", "ripetizione"]
L2 = ["comune", "altro", "esempio", "nuovo"]

print("Elementi comuni: ", listaIntersezione(L1, L2))
print("Elementi non comuni: ", listaUnione(L1, L2))
print("L'indice di Jaccard è: ", Jaccard(L1, L2))