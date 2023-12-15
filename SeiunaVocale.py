"""
Esercizio 004
Sei una Vocale?

Scrivi un programma che chieda all'utente una stringa composta da un solo carattere e dica se si tratta di una vocale oppure no.
"""
# Input del carattere da verificare
car = str(input("Inserisci un carattere: "))

# Definisco una string di nome Vocali contenenti le vocali
Vocali = "aeiouAEIOU"

if car in Vocali:
    print("Hai inserito una vocale")
else:
    print("Non hai inserito una vocale")