"""
Realizzare un'applicazione CresceDecresce. L’applicazione ripetutamente chiede all'utente di
inserire un numero intero da tastiera, stampando ad ogni inserimento (a partire dal secondo) 
un messaggio che indica se l’ultimo numero introdotto è più grande 
o più piccolo del precedente. L’applicazione termina quando l’utente
introduce due volte di fila lo stesso numero.
Nota: l’utente introduce sempre almeno due numeri. 
"""

# Variabile penultimo che detiene il penultimo valore inserito
penultimo = int(input("Inserisci il primo intero: "))

# Variabile ultimo che detiene l'ultimo valore inserito
ultimo = int(input("Inserisci il secondo intero: "))

while (ultimo!=penultimo):
    if ultimo>penultimo:
        print("Questo è più grtande")
    else:
        print("Questo è più piccolo")

    penultimo = ultimo
    ultimo = int(input("Dammi un altro intero: "))

print("Sei diventato ripetitivo!")
