"""
Scrivere un'applicazione MinimoComuneMultiplo che legge due interi da tastiera e ne calcola il minimo comune multiplo. 
Tale valore viene stampato sullo schermo dell'utente.
"""

print("Calcolo del minimo comune multiplo tra due interi")
num1 = int(input("Inserire il primo numero: "))
num2 = int(input("Inserire il secondo numero: "))

# Inizializzo i multiplo_1 e multiplo_2 alla "base", ovvero rispettivamente primo e secondo numero
multiplo1 = num1
multiplo2 = num2

# Trovo il valore minore tra i due
if num1 < num2:
      min = num1
else:
      min = num2

# Ciclo finché i numeri sono diversi tra loro, esco quando sono uguali e quel valore è l'mcm
for i in range(2, min + 1):
        while multiplo1 % i == 0 and multiplo2 % i == 0:
            multiplo1 //= i
            multiplo2 //= i

mcm = abs(num1 * num2)

print("L'mcm tra ", num1, " e ", num2, "è: ", mcm)