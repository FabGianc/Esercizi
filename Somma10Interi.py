"""
Scrivere un'applicazione Somma10Interi che chiede all'utente di inserire 10 interi di cui l'applicazione stampa la somma.
"""

# Variabile contatore per l'iterazione fino a 10 
i = 1

# Variabile per la somma dei 10 valori
somma = 0

# Input 
print("Inserisci 10 valori interi ...")

while i < 11:
    print(f"Inserisci il {i}^ valore intero")
    somma += int(input())
    i+=1

print(f"Somma dei 10 valori interi è: {somma}")

