"""
Scrivere un'applicazione Collatz che legge un intero positivo
introdotto dall'utente e ripetutamente esegue le seguenti azioni:
Se il numero corrente è pari lo divide per 2, altrimenti lo
moltiplica per 3 e gli somma 1; il nuovo numero viene quindi
stampato. L'iterazione termina quando il numero corrente vale 1.
"""

# Input del valore del quale voglio stampare la sequenza
numero = int(input("Inserisci un numero: "))

while (numero != 1):
    print(f"{numero} ", end="")
    # Calcolo il prossimo numero della sequenza
    if (numero%2==0):
        numero = numero // 2
    else:
        numero = 3 * numero +1

print(f"{numero}")