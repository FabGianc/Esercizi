"""
Scrivere un'applicazione NDispari che chiede all'utente di inserire un intero positivo n da tastiera 
e stampa i primi n interi positivi dispari.
"""
# Variabile n di input che conterrà il valore intero positivo
n = -1

# Verifico che  l'input sia maggiore di zero
while n < 1:
    n = int(input("Inserisci un valore intero positivo "))

# Variabile contatore, devo stampare i primi n interi positivi dispari
i = 1

# Ciclo while che stampa gli n interi dispari
while n > 0:
    if i%2 != 0:
        print(i)
        n-=1
    i+=1