""" Programma che data una stringa s i cui simboli sono caratteri alfabetici
minuscoli restituisca la versione maiuscola di s """

s = input("Caro utente, inserisci una stringa di caratteri minuscoli: ")

i = 0 #Indice di scorrimento della string in input

distanzaMinuscoleMaiuscole = ord('A') - ord('a')
maiuscola = ""
while(i < len(s)):
    maiuscola += chr(ord(s[i]) + distanzaMinuscoleMaiuscole)
    i=i+1
    
print(f"Input: {s} --> Output: {maiuscola}")