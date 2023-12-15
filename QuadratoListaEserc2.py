"""
Scrivere un programma che, data una lista di interi Lista e un intero Soglia, 
memorizzi in una variabile intera Risultato la somma dei quadrati dei valori nella lista 
il cui modulo è maggiore di Soglia.  Non è consentita l'inclusione di librerie.
Non è consentita la definizione di funzioni
"""

# Inizializza la lista di interi
Lista = [1, 2, -3, 4, -5, 6, -7]

# Inizializza la soglia
Soglia = 3

# Inizializza la variabile Risultato
Risultato = 0

# Itera attraverso gli elementi della lista
for valore in Lista:
    # Verifica se il valore è maggiore della soglia o il suo opposto è maggiore della soglia
    if valore > Soglia or -valore > Soglia:
        # Aggiungi il quadrato del valore alla somma
        Risultato += valore**2

# Stampa il risultato
print("La somma dei quadrati dei valori il cui modulo è maggiore di", Soglia, "è:", Risultato)
