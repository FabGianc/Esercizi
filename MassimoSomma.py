"""
Scrivere un'applicazione MassimoSomma che ripetutamente chiede all'utente di scrivere numeri interi positivi. 
Quando l'utente inserisce un numero negativo o nullo, l'applicazione termina indicando all'utente qual è il massimo 
fra i numeri inseriti e qual è la loro somma.
"""
# Variabile per contenere il valore massimo
max = 0

# Variabile per la somma dei valori immessi
somma = 0

# Inizializzo la variabile di input a 1, numero negativo o nullo servirà per uscire dal ciclo
n = int(input("Inserisci dei numeri interi (numero negativo o nullo per finire): "))

# Chiedo in input dei valori finchè non viene inserito numero negativo o nullo per cessare
while n > 0:
    # Calcolo la somma
    somma += n
    n = int(input("Inserisci dei numeri interi (numero negativo o nullo per finire): "))
    # Assegno a max il valore più grande
    if max < n:
        max = n

print(f"{somma} è la somma dei valori inseriti mentre {max} è il valore massimo")

 