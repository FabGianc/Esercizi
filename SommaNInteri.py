"""
Scrivere un'applicazione SommaNInteri che chiede all'utente di inserire un intero n 
e poi di inserire n interi di cui l'applicazione stampa la somma.
"""

# Variabile n di input che conterrà il valore intero (positivo) 
n = -1

# Verifico che l'input sia maggiore di zero perchè servirà per gli n inserimenti
while n < 1:
    n = int(input("Quanti valore vuoi inserire (immettere un numero positivo)? "))

# Variabile contatore per l'iterazione fino a n 
i = 1

# Variabile per la somma degli n valori
somma = 0

# Input 
while i <= n:
    print(f"Inserisci il {i}^ valore intero")
    somma += int(input())
    i+=1

print(f"Somma dei valori inseriti è: {somma}")