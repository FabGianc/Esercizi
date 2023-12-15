"""
Scrivere un programma Python che contiene una funzione
trovaListaMassima che presa in input una lista (non vuota) di liste di
numeri restituisce la lista la somma dei cui elementi sia massima.
"""

def trovaListaMassima(Lista):
    sommaMax = -1
    listaMax = []
    for i in Lista:
        print(i)
        print(sum(i))
        if sommaMax < sum(i):
            sommaMax = sum(i)
            listaMax = i
    return listaMax
    
liste_numeri1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

liste_numeri2 = [
    [4, 42, 3],
    [84, 95, 26],
    [17, 8, 29],
    [1, 14, 12]
]

print(__name__)
if __name__ == "__main__":
    print("La lista la cui somma degli elementi sia massima è: ", 
          trovaListaMassima(liste_numeri1))
    print("La lista la cui somma degli elementi sia massima è: ", 
          trovaListaMassima(liste_numeri2))
