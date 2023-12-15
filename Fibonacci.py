"""
Scrivere un frammento di codice che, dato un numero naturale N,
calcola e visualizza i primi N numeri di Fibonacci
    • i primi due numeri di Fibonacci valgono 1
    • ciascun altro numero di Fibonacci è dato dalla somma dei due numeri di Fibonacci che lo precedono
    • i primi numeri di Fibonacci sono 1, 1, 2, 3, 5, 8, 13, 21, …
"""

print("Calcolo dei numeri di Fibonacci")

N = int(input("Inserisci un valore intero: "))

if N <=2:
    print("I primi due numeri di Fibonacci valgono 1 ")
else:
    print("1 1 ", end='')
    F1 = 1
    F2 = 1
    for i in range(3, N+1):
        Fibonacci = F1 + F2
        print(Fibonacci, end=' ')
        F2 = F1
        F1 = Fibonacci




