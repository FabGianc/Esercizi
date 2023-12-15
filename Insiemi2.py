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

# listaIntersezione legge gli elementi della prima lista e li confronta
# con quellio della seconda, se trova un elemento comune lo copia nella nuovaLista
def listaIntersezione(L1,L2):
    # Inizializzaìo la lista che conterrà gli elementi comuni
    listaInter = []
    # Itero lungo gli elementi della lista L1
    for i in range(0, len(L1)):
        # Itero lungo gli elementi della lista L2
        for j in range(0, len(L2)):
            # Se trovo due elementi comuni, inserico in nuova lista
            if L1[i] == L2[j]:
                listaInter.append(L1[i])
    # Restituisco la nuova lista
    return listaInter

def listaUnione(L1,L2):
    # Inizializzaìo la lista che conterrà gli elementi non comuni
    listaU = []
    # Itero lungo gli elementi della lista L1
    for i in range(0, len(L1)):
        # Itero lungo gli elementi della lista L2
        for j in range(0, len(L2)):
            # Se trovo due elementi non comuni, inserico in nuova lista
            if L1[i] != L2[j]:
                listaU.append(L1[i])
    # Restituisco la nuova lista
    return listaU

L1 = ["problema", "esempio", "comune", "ripetizione"]
L2 = ["comune", "altro", "esempio", "nuovo"]

print("Elementi comuni: ", listaIntersezione(L1, L2))
print("Elementi non comuni: ", listaUnione(L1, L2))



