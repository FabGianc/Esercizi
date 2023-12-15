"""
Scrivere un'applicazione MassimoNInteri che chiede all'utente di inserire un intero n 
e poi di inserire n interi di cui l'applicazione stampa il massimo.
"""

# Variabile n di input che conterrà il valore intero (positivo) 
n = -1

# Verifico che l'input sia maggiore di zero perchè servirà per gli n inserimenti
while n < 1:
    n = int(input("Quanti numeri vuoi inserire (immettere un valore positivo)? "))

# Variabile del massimo
max = int(input("Inserisci il 1^ valore intero\n"))

# Variabile contatore per l'iterazione fino a n 
i = 2

# Input 
while i <= n:
    print(f"Inserisci il {i}^ valore intero")
    x = int(input())
    if max < x:
        max = x
    i+=1

print(f"Il valore massimo tra {n} inseriti è: {max}")