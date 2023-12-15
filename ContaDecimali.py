"""
Calcola il numero di cifre nella rappresentazione decimale di un numero naturale n dato
    • Vincolo: non è possibile convertire n in stringa e leggerne la lunghezza con len()
    • Suggerimento: occorre contare quante volte è possibile dividere n per dieci
        (divisione intera) fino ad ottenere zero
    • ad esempio:
        13023//10 → 1302//10 → 130//10 → 13//10 → 1//10 → 0
        13023 è formato da cinque cifre
"""

n = int(input("inserisci un valore intero: "))
intero = n

conta = 0

while n > 0:
    n = n // 10
    conta += 1
    print(n)

print(f"L'intero {intero} è formato da {conta} decimali")