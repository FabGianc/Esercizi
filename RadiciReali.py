import math


"""input"""
print("Ciao utente, introduci i coefficienti di una")
print("        equazione di secondo grado.")
a = float(input())
b = float(input())
c = float(input())

"""output"""
if(a==0):
    print("Funziono solo se 'a' non vale 0!")
else:
    d = b*b-4*a*c

    if(d>0):
        x1 = (-b-math.sqrt(d))/(2*a)
        x2 = (-b+math.sqrt(d))/(2*a)
        print("Ci sono due soluzioni reali distinte pari a {} ed a {}.".format(x1, x2))

    if(d==0):
        x1 = (-b)/(2*a)
        print("Ci sono due soluzioni reali coincidenti pari a {}.".format(x1))

    if(d<0):
        print("Non ci sono soluzioni reali.\n");



