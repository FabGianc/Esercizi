"""
Esercizio 008
Generatore di Istogrammi

Scrivi una semplice funzione che, data una lista di numeri, fornisca in output un istogramma basato su questi numeri, 
usando asterischi per disegnarlo.

Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:

***

*******

*********

*****
"""

Lista = [3, 7, 9, 5]
j = 0

for i in range (0, len(Lista)):
    while j <= Lista[i]:
        print("*", end='')
        j+=1
    print()
    j = 0