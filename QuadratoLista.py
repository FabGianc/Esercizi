"""
Scrivere un programma che, data una lista di interi Lista e un intero Soglia, 
memorizzi in una variabile intera Risultato la somma dei quadrati dei valori nella lista 
il cui modulo è maggiore di Soglia.  Non è consentita l'inclusione di librerie.
Non è consentita la definizione di funzioni
"""

# Inizializza la lista di interi
Lista = [11, -12, 1, -1, -3]

Soglia = 4

Risultato = 0

for e in Lista:
    if e>= Soglia or -e >= Soglia:
        Risultato+=e*e
    
print(Risultato)