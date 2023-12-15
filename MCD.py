""" Programma che legge due interi e informa l'utente sul
massimo comun divisore fra i due interi letti """

print("Caro utente, introduci due interi: ")
x = int(input())
y = int(input())

if(x<y):
    risultato = x
else:
    risultato = y

while (x%risultato !=0 or y%risultato != 0):
    risultato=risultato-1
    
print(f"Il MCD fra {x} e {y} vale {risultato}.")