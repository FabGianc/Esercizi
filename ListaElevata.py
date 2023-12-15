"""
Definire una funzione listaElevata(l,a) che data una lista l di interi e un intero positivo a 
restituisce una nuova lista che contiene gli elementi di l elevati ad a. 
Ovvero, l'elemento in posizione i della nuova lista deve corrispondere all'elemento in posizione i di l elevato ad a.
 
Nota: non è possibile utilizzare la funzione pow.
"""

def listaElevata(l,a):
    # Inizializzo la nuova_lista che conterra gli elemento elevati a potenza di a
    nuova_lista = []

    # Ciclo per tutti gli elementi di l
    for i in range(0, len(l)):
        # Alla nuova_lista aggiungo l'elemento di l[i] elevato ad a
        nuova_lista.append(l[i]**a)
    
    # Restituisco la nuova_lista con gli elementi di l elevati a potenza di a
    return nuova_lista

print(listaElevata([1],10))
print(listaElevata([2,7,3,4],2))
print(listaElevata([-2,2,9,12],3))
print(listaElevata([2,4,8,14],4))
print(listaElevata([2,4,8,14],0))
