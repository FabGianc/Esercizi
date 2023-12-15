"""
Scrivere un'applicazione MeseAnno che chiede all'utente di inserire 2 interi m ed a da tastiera, 
li legge e stampa un messaggio che informa l'utente su quale sia il mese successivo al mese m dell'anno 
a (ad esempio se l'utente introduce m = 10 ed a =2016, il messaggio stampato deve essere del tipo 
"11/2016").
"""
# Il metodo .split() suddivide la stringa inserita in una lista di stringhe ...  
m,a = input("Inserisci mese e anno separati da spazi: ").split()

# ... che vengono poi convertite in numeri interi.
a=int(a)
m=int(m)

if m>0 and m<12:
    print(f"{m+1}/{a}")
else:
    print(f"1/{a+1}")