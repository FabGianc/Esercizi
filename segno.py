"""
Scrivere un'applicazione Segno che chiede all'utente di inserire un intero da tastiera, 
lo legge e stampa un messaggio che dice all'utente se l'intero è positivo, negativo o nullo.
"""

num = int(input("Inserisci un numero: "))

if num > 0:
    print(num, "è positivo")
elif num < 0:
    print(num, "è negativo")
else:
    print(num, "è nullo")