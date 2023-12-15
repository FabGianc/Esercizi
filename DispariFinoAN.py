"""
Scrivere un'applicazione DispariFinoAN che chiede all'utente di inserire un intero positivo da tastiera 
e stampa tutti gli interi dispari minori o uguali dell'intero letto.
"""

# Variabile N di input che conterrà il valore intero positivo
n = -1

# Variabile contatore
i = 1

# Verifico che  l'input sia maggiore di zero
while n < 1:
    n = int(input("Inserisci un valore intero positivo "))

# Ciclo while che stampa gli interi dispari fino a n
while i <= n:
    if i%2 != 0:
        print(i)
    i+=1
