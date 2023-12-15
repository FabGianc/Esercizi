"""
Scrivere un'applicazione PrimiNFibonacci che chiede all'utente di inserire un intero N non negativo
da tastiera e stampa i primi N numeri di Fibonacci
"""

n = int(input("Inserisci un intero non negativo: "))

F=[1,2]
for i in range(2,n):
    F.append(F[i-1]+F[i-2])

if(n>0):
    print(f"I primi {n} numeri di Fibonacci sono ", end="")

for i in range(0,n):
    print(F[i], end=" ")

print()