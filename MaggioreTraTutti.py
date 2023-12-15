"""
Esercizio 003
Il Maggiore tra Tutti!

Scrivi un programma che, data una lista di numeri, fornisca in output il maggiore tra tutti gli elementi della lista.
"""
# Creo una lista di nome Lista
Lista = [16, 8, 1, 3, 5, -5, 9, 89]

# Assegno a Max il primo valore della lista
Max = Lista[0]

for num in Lista:
    if Max < num:
        Max = num

print(f"{Max} è il numero maggiore tra tutti nella lista!")