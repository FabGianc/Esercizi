""" 
Scrivere un'applicazione GiornoMeseAnno che chiede all'utente di inserire 3 interi g, m ed a 
da tastiera, li legge e stampa un messaggio che informa l'utente su quale sia il giorno 
successivo al giorno g del mese m dell'anno a (ad esempio se l'utente introduce 
g= 31, m = 10 ed a =2016, il messaggio stampato deve essere del tipo "1/11/2016").
"""
# Alcune verifiche preliminari:
# ... dapprima inizializzo variabile bool per la correttezza dei dati inseriti
corretto = True

# ... poi ciclo finchè non ottengo dati immessi corretti
while corretto:
    # Input dei dati, il metodo .split() suddivide la stringa inserita in una lista di stringhe ...  
    g,m,a = input("Inserisci giorno, mese e anno separati da spazi: ").split()

    # ... che vengono poi convertite in numeri interi.
    g = int(g)
    m = int(m)
    a = int(a)
   
    # Verifico se l'anno è bisestile ...
    bisestile = ((a%4 == 0) and (a%100 != 0)) or a%400 == 0
    
    # ... poi se è un mese di 30 giorni
    trenta = m == 4 or m == 9 or m == 9 or m == 11
    
    if m==2 and bisestile and g>29:
        print("Valore errato: l'anno è bisestile, quindi febbraio ha massimo 29 giorni")
    elif m==2 and not(bisestile) and g>28:
        print("Valore errato: l'anno non è bisestile, quindi febbraio ha massimo 28 giorni")
    elif trenta and g>30:
        print("Valore errato: il mese ha massimo 30 giorni")
    elif not(trenta) and g>31:
        print("Valore errato: il mese ha massimo 31 giorni")
    elif m>12:
        print("Valore errato: l'anno ha massimo 12 mesi")
    else:
        # Esco dal ciclo
        corretto = False

# Se l'anno è bisestile e se il mese è febbraio ...
if m==2 and bisestile:
    # ... se i giorni sono 28
    if g==28:
        # ... allora giorni diventano 29
        g+=1
    # ... se i giorni sono 29
    elif g==29:
        # ... allora giorni diventa 1 e mese +1
        g=1
        m+=1
    print(f"{g}/{m}/{a}")

# ... invece se l'anno non è bisestile, se il mese è febbraio e se i giorni sono 28 ...
elif m==2 and not(bisestile) and g==28:
    # ... allora giorni diventa 1 e mese +1
    g=1
    m+=1
    print(f"{g}/{m}/{a}")

# ... se è San Silvestro: aumento anno, mentre metto a 1 giorno e mese
elif g == 31 and m == 12:
    g = 1
    m = 1
    a+=1
    print(f"{g}/{m}/{a}")

# ... se mese da 30 e giorni 30: aumento mese e giorni va a 1   
elif g == 30 and trenta:
    g = 1    
    m+= 1
    print(f"{g}/{m}/{a}")

# ... se mese da 31 e giorni 31: aumento mese e giorni va a 1
elif g == 31 and not(trenta):
    g = 1
    m+= 1
    print(f"{g}/{m}/{a}")
# ... per tutto il resto c'è mastercard :-))
else:
    print(f"{g+1}/{m}/{a}")