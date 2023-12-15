"""
Scrivere un'applicazione StampaPariCompresi che chiede all'utente di
inserire due interi a e b da tastiera. L’applicazione stampa tutti i numeri
pari compresi fra il più piccolo ed il più grande fra a e b, dopo aver
stampato un’opportuna frase introduttiva.
Se fra i numeri che vengono stampati è presente la somma fra a e b, allora
l’applicazione stampa un ulteriore messaggio a riguardo, subito dopo aver
stampato il numero stesso.
"""

print("Inserici due interi ")

# Input
a = int(input("Primo numero: "))
b = int(input("Secondo numero: "))

# Verifico quale dei due è il minore perhè è il mio valore di partenza
if a>b:
    max = a
    min = b
else:
    max = b
    min = a

# Stampo tutti i numeri pari compresi fra il più piccolo ed il più grande fra a e b
for i in range(min,max+1):
    if (i%2 == 0):
        print(f"{i} ", end="")
        # Verifico se fra i numeri che vengono stampati è presente la somma fra a e b
        if (i==a+b):
            print(f"(questo numero è pari alla somma tra {a} e {b}) ", end="")