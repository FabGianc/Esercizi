"""
Scrivere un programma Python che contiene una funzione isPalindroma
che prende in input una stringa s e restituisce True se e solo se s è
palindroma. Il programma contiene inoltre una funzione
quantePalindromePari che prende in input una lista di stringhe e
determina il numero di stringhe palindrome di lunghezza pari in essa
contenute.
"""

def isPalindroma(s):
    i = 0 
    j = len(s) - 1
    
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    
    return True

def quantePalindromePari(lista):
    palind = 0
    i = 0
    while i < len(lista):
        if isPalindroma(lista[i]) and len(lista[i]) % 2 == 0:
            palind += 1
        i += 1
    return palind

Lista =["ciao", "cc", "aba", "caac", "anna"]

print(quantePalindromePari(Lista))