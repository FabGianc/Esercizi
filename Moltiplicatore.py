"""Realizzare un programma Moltiplicatore che legge due numeri reali introdotti
dall'utente e stampa sullo schermo un numero reale pari al prodotto
dei due numeri reali letti."""

#Chiedo in input i due numeri reali
print("Inserisci due valori reali da moltiplicare:")
num1 = float(input("Primo numero:"))
num2 = float(input("Secondo numero:"))

#Stampo a video il risultato
print("{} è il prodotto tra {} e {}".format(num1*num2, num1, num2))