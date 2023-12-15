"""
Scrivere un'applicazione CoppieDivisibiliPerTre che chiede all'utente di inserire un
intero N da tastiera e stampa tutte le coppie (i,j) tali che 1 ≤ 𝑖 ≤ 𝑗 ≤ 𝑛 e i+j è
divisibile per 3
"""

# Variabile numero per l'inserimento dell'utente
# i, j variabili che conterranno le coppie

numero = int(input("Inserisci un intero: "))

print("Ecco le tue coppie: ")

for i in range(1,numero+1):
    print(f"Coppie il cui valore vale {i} ", end='')
    for j in range(1, numero +i):
        # Verifico se i+j è divisibile per 3
        if (i+j)%3==0:
            print(f"({i}, {j}) ", end='')
    print()
