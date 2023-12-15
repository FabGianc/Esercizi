"""
Funzione che determina se un intero è un quadrato oppure no,
restituendo 1 oppure 0 rispettivamente
"""
def isQuadrato(intero):
    risultato = False

    radice = 1
    while(radice*radice<=intero and not risultato):
        if (radice*radice==intero):
            risultato = True
        else:
            radice += 1

    return risultato

print(isQuadrato(14))