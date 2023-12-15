"""
Scrivere un'applicazione MCDEuclide che chiede all'utente di inserire due interi da tastiera e ne calcola il massimo comun divisore 
utilizzando l'algoritmo di Euclide. L'algoritmo di Euclide ripetutamente svolge le seguenti tre istruzioni: 
1) calcola il resto fra il massimo ed il minimo fra i due numeri; 
2) aggiorna il valore del massimo fra i due numeri al valore del minimo; 
3) aggiorna il valore del minimo fra i due numeri al valore del resto. 
L'algoritmo termina quando il resto è zero. Allora il risultato è il valore memorizzato nel massimo fra i due numeri.
"""
# Input di a e b
print("Calcolo del MCD tra due numeri ...")
num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

# resto è uguale al resto tra i due valori num1 e num2
# quindi assegno ad num1 il valore di num2
# e assegno a num2 il resto

while(num2 != 0):
        resto=num1%num2
        num1=num2
        num2=resto

print(num1)