"""
Scrivere un'applicazione Somma10Interi che chiede all'utente di inserire 10 interi di cui l'applicazione stampa la somma.
"""

# Variabile per la somma dei 10 valori
somma = 0

# Input 
print("Inserisci 10 valori interi ...")

for i in range (1,11):
    print(f"Inserisci il {i}^ valore intero")
    somma += int(input())

print(f"Somma dei 10 valori interi è: {somma}")