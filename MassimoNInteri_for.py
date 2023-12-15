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
max = 0

# Input 
for i in range (1, n+1):
    print(f"Inserisci il {i}^ valore intero")
    x = int(input())
    if max < x:
        max = x

print(f"Il valore massimo tra {n} inseriti è: {max}")