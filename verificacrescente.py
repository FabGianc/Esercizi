"""
Definire una funzione verifica_crescente(l) che data una lista di interi l verifica se la sequenza è strettamente crescente.
"""

def verifica_crescente(l):
    # Ciclo attraverso gli elementi della lista l
    for i in range(1, len(l)):
        # Verifico se l'elemento corrente è maggiore o uguale a quello precedente
        if l[i] <= l[i - 1]:
           
            # La sequenza non è strettamente crescente
            return False 

    # La sequenza è strettamente crescente
    return True  

# Esempi di utilizzo:
lista_crescente = [1, 2, 3, 4, 5]
lista_non_crescente = [1, 3, 2, 4, 5]

risultato_crescente = verifica_crescente(lista_crescente)
risultato_non_crescente = verifica_crescente(lista_non_crescente)

print(risultato_crescente)  # Output: True
print(risultato_non_crescente)  # Output: False
