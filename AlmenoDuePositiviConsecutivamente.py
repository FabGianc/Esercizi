"""
Scrivere un'applicazione AlmenoDuePositiviConsecutivamente che ripetutamente chiede all'utente di scrivere numeri interi 
fintanto che l'utente non introduce il numero 0. L'applicazione termina stampando un messaggio che dice all'utente 
se sono stati introdotti (almeno) due numeri positivi consecutivamente oppure no.
"""

# Inizializzo le variabili di input. Poichè la verifica è su coppie di valori inizializzo num1 a 1 che servirà per il primo valore 
# e verifico che non sia 0 per l'uscita immediata dal ciclo. Num2 può essere tranquillamante inizializzata a 1
num1 = 1
num2 = 0

# Inizializzo la variabile booleana che indicherà la prsenza di una coppia du valori positivi oppure no
positivo = False

num1 = int(input("Inserisci dei numeri interi (0 per finire): "))

# Chiedo in input dei valori finchè non viene inserito 0 per cessare
while num1 !=0:
    num2 = num1
    num1 = int(input("Inserisci dei numeri interi (0 per finire): "))
    # Verifico che la coppia sia positiva o meno
    if num1 > 0 and num2 > 0:
        positivo = True

if num1 == 0 and num2 == 0:
    print("Ciao, alla prossima")
elif positivo:
    print("Hai inserito almeno una coppia di valori positivi")
else:
    print("Non hai inserito alcun coppia di valori positivi")