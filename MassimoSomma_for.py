"""
Scrivere un'applicazione MassimoSomma che ripetutamente chiede all'utente di scrivere numeri interi positivi. 
Quando l'utente inserisce un numero negativo o nullo, l'applicazione termina indicando all'utente qual è il massimo 
fra i numeri inseriti e qual è la loro somma.
"""
# Variabile per contenere il valore massimo
max = 0

# Variabile per la somma dei valori immessi
somma = 0

# Poichè con il ciclo for non ho la possibilità di verificare il valore di uscita, devo ricorrere al costrutto break, benchè deprecato
# e quindi iterare per un valore arbitrario
for i in range(100):
    # Input n
    n = int(input("Inserisci dei numeri interi (numero negativo o nullo per finire): "))
    if n < 1:
        break
    # Calcolo la somma
    somma += n
    # Assegno a max il valore più grande
    if max < n:
        max = n

print(f"{somma} è la somma dei valori inseriti mentre {max} è il valore massimo")
