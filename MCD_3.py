"""
Scrivere un frammento di codice per calcolare il massimo comun divisore di due numeri interi positivi N e M dati, 
basato sul seguente algoritmo:
1. Finché N è diverso da M
    • se N è maggiore di M, sostituisci a N il valore di N-M
    • se M è maggiore di N, sostituisci a M il valore di M-N
2. il risultato è N
"""

print("Calcolo del MCD...")
M = int(input("Inserisci il primo intero positivo: "))
N = int(input("Inserisci il secondo intero positivo: "))

while N!=M:
    if N > M:
        N = M
    elif M > N:
        M = N

print("Il massimo comun divisore é: ",N)