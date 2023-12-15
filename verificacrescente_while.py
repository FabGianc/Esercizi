"""
Definire una funzione verifica_crescente(l) che data una lista di interi l verifica se la sequenza è strettamente crescente.
"""

def verifica_crescente(l):
    # Inizializzo l'indice a 1
    i = 1

    # Ciclo finché non raggiungo la fine della lista
    while i < len(l):
        # Verifico se l'elemento corrente è maggiore di quello precedente
        if l[i] <= l[i - 1]:
            # La sequenza non è strettamente crescente
            return False  

        # Incremento l'indice
        i += 1

    # La sequenza è strettamente crescente
    return True  

# Esempi di utilizzo:
lista_crescente = [1, 2, 3, 4, 5]
lista_non_crescente = [1, 3, 2, 4, 5]

risultato_crescente = verifica_crescente(lista_crescente)
risultato_non_crescente = verifica_crescente(lista_non_crescente)

print(risultato_crescente)  # Output: True
print(risultato_non_crescente)  # Output: False
