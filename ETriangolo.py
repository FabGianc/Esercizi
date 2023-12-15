"""
Scrivere un'applicazione ETriangolo che chiede all'utente di inserire 
3 interi a, b e c da tastiera, li legge e stampa un messaggio che dice 
all'utente se i tre numeri rappresentano oppure no le misure dei lati di un triangolo 
(3 numeri formano i lati di un triangolo se sono tutti positivi e ciascuno è minore della 
somma degli altri due).
"""

print("Inserisci tre valori per gli angoli")
a=int(input("Primo lato: "))
b=int(input("Secondo lato: "))
c=int(input("Terzo lato: "))

if a<1 or b<1 or c<1:
    print("Non è un triangolo")
elif a<(b+c) and b<(a+c) and c<(a+b):
    print("E' un triangolo")
else:
    print("Non è un triangolo")