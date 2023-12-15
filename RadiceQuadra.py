"""
Scrivere un frammento di codice che, dato un numero naturale N,
calcola la radice quadrata intera R di N, (eventualmente approssimata per difetto)
    • R è il più grande numero naturale il cui quadrato è minore o uguale a N (cioè R al quadrato <= N)
"""

print("Calcolo della radice quadrata intera R di N ...")

# Input del valore N
N = int(input("Insersci un numero naturale: "))

# Inizializzo la variabile R, ovvero la radice quadrata intera
R = 0

# Itero finchè R*R <= N
while R*R <= N:
    R += 1

print(f"La radice quadrata intera R di {N} è: {R}")