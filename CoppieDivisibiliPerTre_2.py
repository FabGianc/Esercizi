"""
Scrivere un'applicazione CoppieDivisibiliPerTre che chiede all'utente di inserire un intero n da tastiera 
e stampa tutte le coppie (i,j) tali che 1<=i<=j<=n e tali che i+j è divisibile per 3.
"""

n = int(input("Inserisci un valore intero: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if (i+j)%3==0:
            print(i,' ',j)