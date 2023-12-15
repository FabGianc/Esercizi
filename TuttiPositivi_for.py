"""
Scrivere un'applicazione TuttiPositivi che chiede all'utente di inserire un intero n e poi di inserire n interi. 
L'applicazione stampa un messaggio in cui dice all'utente se tutti gli interi inseriti sono positivi oppure no.
"""

# Variabile n di input che conterrà il valore intero (positivo) 
n = -1

# Verifico che l'input sia maggiore di zero perchè servirà per gli n inserimenti
while n < 1:
    n = int(input("Quanti numeri vuoi inserire (immettere un valore positivo)? "))

# Input 
for i in range (1, n+1):
    print(f"Inserisci il {i}^ valore intero")
    if int(input()) > 0:
        print("L'intero è valore positivo")
    else:
        print("L'intero non è valore positivo")