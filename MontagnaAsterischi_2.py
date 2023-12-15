"""
Scrivere un'applicazione MontagnaAsterischi che chiede all'utente di inserire un intero da tastiera e stampa una montagna di asterischi
 la cui altezza è pari all'intero inserito dall'utente.
"""
# Input
n = int(input("Inserisci l'altezza della montagna con un numwero intero: "))

for i in range(n+1, 1,-1):
    print("*")

for j in range(1, n+1):
    print("-", end="")
    