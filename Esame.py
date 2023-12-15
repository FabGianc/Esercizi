"""
Scrivere un programma che, data una lista di interi Lista e un intero Soglia, 
memorizzi in una variabile intera Risultato la somma dei quadrati dei valori 
nella lista il cui modulo è maggiore di Soglia.
Il modulo di un numero n coincide con n se n>=0 e con -n se n<0.
Per esempio, con Lista=[10,-7,2,-3,-5] e Soglia=4, i valori della lista il cui 
quadrato contribuisce al valore di Risultato sono 10,-7, e -5. La variabile intera Risultato dovrà quindi contenere il valore (10)2 + (-7)2 + (-5)2 = 100 + 49 + 25 = 174 al termine dell'esecuzione del programma.

Nota: 
    Non è consentito l'uso di istruzioni print e input diverse da quelle già presenti.
    Non è consentita l'inclusione di librerie.
    Non è consentita la definizione di funzioni.
"""

Lista=[10,-7,2,-3,-5]

Soglia=4

# Inizializzo la variabile Risultato
Risultato = 0

# Itero per tutti i valori in Lista 
for valore in Lista:
    # Verifico se il valore è maggiore della soglia o 
    # il suo opposto è maggiore della soglia
    # --> si sarebbe potuta usare la funzione abs()
    if valore > Soglia or -valore > Soglia:
        # Aggiungo il quadrato del valore alla somma
        Risultato += valore**2

print(Risultato)