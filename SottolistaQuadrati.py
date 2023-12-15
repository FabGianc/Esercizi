"""
Definire una funzione sottolistaQuadrati(l) che data una lista l di interi restituisce una nuova lista 
che contiene gli elementi di l che sono quadrati di un intero nell'ordine in cui appaiono in l.
"""

# Definisco una funzione che dato un intero, restitusce True se è un quadrato o False se viceversa
def isQuadrato(intero):
    # Inizializzo l variabili ...
    # ... non ho trovato il quadrato, quindi risultato = False
    risultato = False

    # Verifico tutti gli interi finchè non eccedo il valore intero
    radice = 1
    while(radice*radice<=intero and not risultato):
        if (radice*radice==intero):
            # E' un quadrato
            risultato = True
        else:
            # Non è un quadrato, continuo a iterare
            radice += 1

    # Restituisco il risultato
    return risultato

# Funzione che itera e verifica ciascun elemento alla ricerca di un quadrato
def sottolistaQuadrati(l):
    # Inizializzo la nuova_lista che conterrà i quadrati trovati
    nuova_lista = []
    # Ciclo per tutta la lista l
    for i in range(0, len(l)):
        # Verifico se l'i-esimo elemento è un quadrato ...
        if isQuadrato(l[i]):
            # ... in caso positivo lo accodo alla nuova_lista
            nuova_lista.append(l[i])

    # Restituisco la nuova_lista con i quadrati trovati
    return nuova_lista

print(sottolistaQuadrati([]))
print(sottolistaQuadrati([2,36,14,16]))
print(sottolistaQuadrati([2,-36,14,-16]))
print(sottolistaQuadrati([2,-25,64]))
print(sottolistaQuadrati([100]))