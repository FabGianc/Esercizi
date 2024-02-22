"""
Ciascun dato anagrafico è un 
dizionario con le seguenti chiavi:
'nome'
'cognone'
'data di nascita'
'residenza'
"""
import json

anagrafica = {}
print("Inserisci i dati anagrafici ...")
anagrafica["nome"] = input("Nome: ")
anagrafica["cognome"] = input("Cognome: ")
anagrafica["data"] = input("Data di nascita (gg/mm/aaaa): ")
anagrafica["residenza"] = input("Residenza: ")

# print(anagrafica)

def serializza(anagrafica):
    # json.dumps: serializza in JSON un oggetto Python e restituisce la stringa
    # corrispondente in formato JSON.

    json_string = json.dumps(anagrafica, indent = 4)
    return (json_string)

stringa_json = serializza(anagrafica)

print(stringa_json)

def deserializza(stringa_json):
    # json.loads() può essere utilizzato per analizzare una stringa JSON valida
    # e convertirla in un dizionario Python.
    #   • Utile per deserializzare stringhe ottenute dalla rete.
    
    dizionario = json.loads(stringa_json)
    # print(type(dizionario)) # stampa <class 'dict'>
    return (dizionario)

print(deserializza(stringa_json))