"""
Scrivere un'applicazione MassimoSomma che ripetutamente chiede
all'utente di scrivere numeri interi positivi. Quando l'utente inserisce un
numero negativo o nullo, l'applicazione termina indicando all'utente qual è il
massimo fra i numeri inseriti e qual è la loro somma.
Nota: Il numero negativo o nullo che termina l'esecuzione dell'applicazione
non deve essere conteggiato nella somma
"""

numero = int(input("Inserisci dei numeri interi (numero negativo o nullo per finire): "))

massimo = 0
somma = 0

while (numero>=1):
    somma += numero
    if (numero>massimo):
        massimo = numero
    numero = int(input("Dammi un altro numero: "))

if (massimo > 0):
    print(f"La somma dei valori da te inseriti è pari a {somma}")
    print(f"Il massimo dei valori da te inseriti è pari a {massimo}")
else:
    print("Non hai introdotto nessun numero positivo!")