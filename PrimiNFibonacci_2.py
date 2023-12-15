"""
Scrivere un'applicazione PrimiNFibonacci che chiede all'utente di inserire un intero N non negativo
da tastiera e stampa i numeri di Fibonacci minori di N
Nota non ci sono numeri di Fibonacci (stretttament) miniri di 1
Quindi l'applicazione poroduce una sequanza di output solo se N>=2
"""

n = int(input("Inserisci un intero non negativo: "))
        
F = [1,1]

while(F[len(F)-1] + F[len(F)-2] <n):
    F.append(F[len(F) -1] + F[len(F) -2])

if (n>1):
    print(f"I numeri di Fibonacci minori si {n} sono ", end="")
    for g in F:
        print(g, end=" ")