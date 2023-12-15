"""
Sia anno una variabile intera che rappresenta un anno. Scrivere
una espressione booleana, in cui compare la variabile anno, che è
vera se e solo se anno è bisestile.
• normalmente, anno è bisestile se è divisibile per 4 è cioè la divisione
  da resto 0
• ma se è anche divisibile per 100 allora non è bisestile è come nel
  caso dell'anno 1900
• nonostante le condizioni precedenti, se anno è divisibile per 400
  allora è bisestile è come nel caso dell'anno 2000

"""

#INPUT
anno = int(input("Inserisci l'anno da verificare "))

#Verifico se bisestile e stampo il risultato
b = ((anno%4 == 0) and (anno%100 != 0)) or anno%400 == 0
print(b)