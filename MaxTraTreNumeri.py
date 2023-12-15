"""
Esercizio 002
Max tra Tre Numeri

Scrivi un programma che chieda tre numeri a, b, c all'utente e mostri il più grande tra loro.
"""

a = int(input("Inserisci il primo valore: "))
b = int(input("Inserisci il secondo valore: "))
c = int(input("Inserisci il primo valore: "))

if a > b and a > c:
    print(f"{a} è il più grande")
elif b > a and b > c:
    print(f"{b} è il più grande")
elif c > a and c > b:
    print(f"{c} è il più grande")
else:
    print("Sono uguali")