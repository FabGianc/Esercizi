"""
Scrivere un'applicazione MontagnaAsterischi che chiede all'utente di inserire un intero 
da tastiera e stampa una montagna di asterischi la cui altezza è pari 
all'intero inserito dall'utente.
"""
# Input varuiabile che rappresenta l'altezza della montagna
h = int(input("Inserisci l'altezza della montagna con un numwero intero: "))

for i in range(h):
    for j in range(h+i):
        if (h-j-1>i): 
            print(' ', end='')
        else:
            print('*', end='')
    print()

# i e j variabili per indicizzare rispettivamente le righe e le colonne della montagna
# Scorro le righe
for i in range(1, h+1):
    for j in range(1, 2*h+1):
        # Verifico se stampa spazio o asterisco
        if (j<=h -i or j>= h +i+1):
            print('  ', end='')
        else:
            print('* ', end='')
    print("")

for i in range(1,h+1):
    print("  "*(h-i)+ "* "*2*i)