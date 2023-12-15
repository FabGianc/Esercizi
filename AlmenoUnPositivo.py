"""
Scrivere un'applicazione AlmenoUnPositivo che ripetutamente chiede all'utente di scrivere numeri interi 
fintanto che l'utente non introduce il numero 0. L'applicazione termina stampando un messaggio 
che dice all'utente è stato introdotto almeno un numero positivo oppure no.
"""

# Inizializzo la variabile di input a 1, 0 servirà per uscire dal ciclo
n = 1

# Inizializzo la variabile booleana che indicherà la prsenza di un valore positivo oppure no
positivo = False

# Chieddo in input dei valori finchè non viene inserito 0 per cessare
while n !=0:
    n = int(input("Inserisci dei numeri interi (0 per finire): "))
    # Verifico che n sia positivo o meno
    if n > 0:
        positivo = True

if positivo:
    print("Hai inserito almeno un valore positivo")
else:
    print("Non hai inserito alcun valore positivo")