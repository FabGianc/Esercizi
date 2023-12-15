"""
Scrivere un'applicazione TipoTriangolo che chiede all'utente di 
inserire 3 interi a, b e c da tastiera, li legge e stampa un messaggio 
che dice all'utente se il triangolo con lati a, b e c è equilatero, isoscele o scaleno.
"""
print("Inserisci tre valori per gli angoli")
a=int(input("Primo lato: "))
b=int(input("Secondo lato: "))
c=int(input("Terzo lato: "))

if a==b and a==c and b==c:
    print("E' un triangolo equilatero")
elif a==b or a==c or b==c:
    print("E' un triangolo isoscele")
else:
    print("E' un triangolo scaleno")