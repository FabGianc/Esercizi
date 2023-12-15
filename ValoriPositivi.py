"""
Definire una funzione valori_positivi(l) che data una lista di interi l 
restituisce una lista formata dai soli valori strettamente positivi contenuti in l.
"""

def valori_positivi(l):
    # Inizializzo una lista vuota che conterrà i valori positivi
    valori_positivi_lista = []

    # Ciclo attraverso gli elementi della lista di input
    for elemento in l:
        # Aggiungoo il valore alla lista solo se è strettamente positivo
        if elemento > 0:
            valori_positivi_lista.append(elemento)

    return valori_positivi_lista

# Esempio di utilizzo:
lista_input = [1, -2, 3, -4, 5, 0, 6]
risultato = valori_positivi(lista_input)
print(risultato)