def cancella(l, i):
    # Verifichiamo se l'indice i è valido
    if 0 <= i < len(l):
        # Creiamo una nuova lista che contiene gli elementi tranne quello in posizione i
        nuova_lista = l[:i] + l[i+1:]
        return nuova_lista
    else:
        # Se l'indice non è valido, restituire la lista originale
        return l

# Esempio di utilizzo:
lista_originale = [1, 2, 3, 4, 5]
indice_da_cancellare = 2

nuova_lista = cancella(lista_originale, indice_da_cancellare)
print(nuova_lista)
