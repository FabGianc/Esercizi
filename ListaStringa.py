"""
Possiamo usare la funzione join() per ricavare una singola stringa a partire
da una lista di caratteri e/o di stringhe in questo modo...
"""

l1 = ['H','e','l','l','o',' ','World']
s = ''.join(l1) # s <- 'Hello World'
print(s) # stampa 'Hello World '
s = '--'.join(list('ciao'))
print(s) # stampa 'c--i--a--o'

print(type(l1))
print(type(s))