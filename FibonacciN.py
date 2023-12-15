"""
Scrivere un frammento di codice che, dato un numero naturale N,
calcola e visualizza i numeri di Fibonacci il cui valore è minore o uguale a N
"""

print("Calcola e visualizza i numeri di Fibonacci il cui valore è minore o uguale a N")

N = int(input("Inserisci valore di N: "))

if N <=2:
    print("I primi due numeri di Fibonacci valgono 1 ")
else:
    print("1 1 ", end='')
    F1 = 1
    F2 = 1
    Fibonacci = F1 + F2
    while Fibonacci <= N:
        print(Fibonacci, end=' ')
        F2 = F1
        F1 = Fibonacci
        Fibonacci = F1 + F2