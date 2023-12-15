"""
prove su liste
"""

wd = ['Pippo', 'Pluto', 'Paperino', 'Minni', 'Topolino']
key = 'Minni'
if (key in wd):
    # la condizione è vera
    print(wd.index(key)) # stampa 3
key = 'Quo'
if (key in wd): 
    # la condizione è falsa
    print(wd.index(key)) # nessuna stampa
key = 'Qua'
print(wd.index(key)) # stampa il seguente errore: ValueError: 'Quo' is not in list