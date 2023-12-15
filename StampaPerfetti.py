"""
Realizzare un’applicazione StampaPerfetti che legge un intero e stampa tutti i
numeri perfetti compresi fra 1 e il numero letto. Un numero si dice perfetto se è
uguale alla somma dei suoi divisori diversi da se stesso. Ad esempio 6 è un numero
perfetto in quanto i suoi divisori sono 1, 2, 3, 6 e vale 6=1+2+3.
"""

def calcolaDivisori(numero):
    divisori = [1]  # Ogni numero è divisibile per 1
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            divisori.append(i)
    return divisori

def stampaNumeriPerfetti(fino_a):
    for num in range(2, fino_a + 1):
        divisori = calcolaDivisori(num)
        if num == sum(divisori):
            print(f"Il numero {num} è perfetto. I suoi divisori sono: {divisori}")

print(__name__)
if __name__ == "__main__":
    numero_input = int(input("Inserisci un numero intero: "))
    stampaNumeriPerfetti(numero_input)
