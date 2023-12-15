"""
GIOCO SCOPA
Realizzare un'applicazione Gioco Scopa. L’applicazione ripetutamente chiede
all'utente di inserire un numero intero da tastiera, fino a quando l’utente non
inserisce un numero che è pari alla somma di tutti i numeri precedentemente
introdotti dall’utente. Quando questo avviene, l’applicazione comunica all’utente
quanti numeri ha inserito (compreso l’ultimo). Nota che l’applicazione può
terminare dopo aver letto un singolo numero, se il primo numero introdotto
dall’utente è zero. 
"""

# Input, chiedo il primo valore inserito dall'utente
numero = int(input("Inserisci un primo intero: "))

# Variabile contatore che detiene il numero degli inserimenti dell'utente
# Inizializzo a 1 perchè l'utente coll'input preedente ha già inserito un vaolre
quanti = 1

# inizializzo variabile somma per il calcolo della somma
somma = 0

# Ciclo fino a quando l’utente non inserisce un numero 
# che è pari alla somma di tutti i numeri precedentemente introdotti
while (numero!=somma):
    somma += numero
    numero = int(input("Inserisci un altro intero: "))
    quanti += 1

print(f"Hai fatto scopa con {quanti} numeri!")