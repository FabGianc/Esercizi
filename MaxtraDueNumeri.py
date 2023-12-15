"""
Esercizio 001
Scrivi un programma che chieda due numeri all'utente tramite la funzione input e mostri il più grande tra i due utilizzando 
la funzione print. 
Per quanto Python disponga di una funzione max(), siete invitati ad utilizzare le istruzioni 
if, elif ed else per la scrittura dell'algoritmo.
"""

a = int(input("Inserisci il primo valore: "))
b = int(input("Inserisci il secondo valore: "))

if a > b:
    print(f"{a} è il più grande")
elif a < b:
    print(f"{b} è il più grande")
else:
    print("Sono uguali")