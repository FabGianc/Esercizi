"""
Scrivere un'applicazione NDispari che chiede all'utente di inserire un intero positivo n da tastiera 
e stampa i primi n interi positivi dispari.
"""
# Variabile n di input che conterrà il valore intero positivo
n = -1

# Verifico che l'input sia maggiore di zero
while n < 1:
    n = int(input("Inserisci un valore intero positivo "))

# Ciclo for che stampa gli n interi dispari
for i in range(1, 2 * n + 1, 2):
        print(i)
       