""" Programma che data una stringa s i cui simboli sono caratteri alfabetici
(senza assumere che la stringa S sia composta da soli caratteri alfabetici minuscoli)
e restituisca la versione maiuscola di s """

# Le lettere maiuscole hanno valore ASCII dal 65 (A) al 90 (Z), mentre
# le lettere minuscole hanno valore ASCII dal 97 (a) al 122 (z) ...
# quindi se ord(carattere) è <= 90 è unq maiuscola, 
# altrimenti una minuscola
# Nota: la distanza tra maiuscolo e minuscolo è di 32 ...
# e lo spazio ha valore 0 e 32, quindi una stringa composta da più parole
# anche gli spazi saranno corettamente trattati.

s = input("Caro utente, inserisci una stringa di caratteri: ")

i = 0 #Indice di scorrimento della string in input

# Inizialiizzo la variabile stringa che conterrà i caratteri maiuscoli
maiuscola = ""

# Ciclo fino alla fine della stringa
while(i < len(s)):
    # Verifico se il carattere corrente è maiusolo ...
    if ord(s[i])<= 90:
        # ... quindi lo aggiungo e basta
        maiuscola += s[i]
    # altrimenti è minuscolo e devo convertirlo prima di aggiungerlo
    else:
        # Sottraggo la distanza per convertire il minuscolo in maiuscolo
        maiuscola += chr(ord(s[i]) - 32)
    # Incremento l'indice
    i=i+1

# Ed ecco il mio output in maiuscolo ...
print(f"Input: {s} --> Output: {maiuscola}")