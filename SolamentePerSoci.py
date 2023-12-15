"""
Esercizio 007
Solamente per Soci

Scrivi un programma che a partire da un elemento e una lista di elementi dica in output 
se l'elemento passato sia presente o meno nella lista.

Qualora l'elemento sia presente nella lista, il programma dovrà comunicarci l'indice dell'elemento tramite il metodo index.
"""
# Input il nome della persona da ricercare
# Converto il testo in minuscolo
socio = str(input("Inserisci il nome della persona: ")).lower()

# Lista dei soci
Lista = ["pippo", "pluto", "paperina", "topolino", "paperino", "minnie"]

if socio in Lista:
    print(f"{socio} è un socio e si trova alla posizione {Lista.index(socio)}")
else:
    print(f"{socio} non è un socio!")
