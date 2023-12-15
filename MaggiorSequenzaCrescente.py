"""
Scrivere un programma Python che contiene una funzione
maggiorSequenzaCrescente che presa in input una lista di interi L
restituisce la più lunga sottosequenza crescente di L
• Per sottosequenza intendiamo una lista fatta da elementi consecutivi di L
"""

def maggiorSequenzaCrescente(L):
    sottoLis = [L[0]]
    sottoLisMax = [L[0]]

    for i in range(1, len(L)):
        if L[i-1] < L[i]:
            sottoLis.append(L[i])
        else:
            sottoLis = [L[i]]
        if len(sottoLis) > len(sottoLisMax):
            sottoLisMax = sottoLis[:]            
    return sottoLisMax



Lista = [2, 3, 7, 1, 2, 3, 4, 6]

print(maggiorSequenzaCrescente(Lista))