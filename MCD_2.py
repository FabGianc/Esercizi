def calcola_mcm(numero1, numero2):
    # Trova il massimo comune divisore (MCD) utilizzando l'algoritmo di Euclide
    a, b = numero1, numero2
    for i in range(2, min(numero1, numero2) + 1):
        while a % i == 0 and b % i == 0:
            a //= i
            b //= i

    # Calcola il MCM utilizzando la formula: MCM(a, b) = |a * b|
    mcm = abs(numero1 * numero2)
    return mcm

def main():
    try:
        # Chiedi all'utente di inserire due interi
        numero1 = int(input("Inserisci il primo intero: "))
        numero2 = int(input("Inserisci il secondo intero: "))
        
        # Calcola il MCM utilizzando la funzione calcola_mcm
        risultato_mcm = calcola_mcm(numero1, numero2)
        
        # Stampa il risultato
        print(f"Il Minimo Comune Multiplo (MCM) di {numero1} e {numero2} è: {risultato_mcm}")
    except ValueError:
        print("Inserisci due interi validi.")

if __name__ == "__main__":
    main()
