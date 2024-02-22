# Client

import socket
import json
from invio_ricezione import lettura_messaggio, invio_messaggio

def inserisci_dato_anagrafico():
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    data_nascita = input("Inserisci la data di nascita: ")
    residenza = input("Inserisci la residenza: ")

    dato_anagrafico = {
        'nome': nome,
        'cognome': cognome,
        'data di nascita': data_nascita,
        'residenza': residenza
    }

    return json.dumps(dato_anagrafico)

def main():
    addr = "127.0.0.1"
    port = 8000

    client = socket.socket()
    client.connect((addr, port))

    print("Invia dati anagrafici al server. Inserisci 'chiudi' per terminare.")
    print("Aspetto un interlocutore...")
    ok = client.recv(2)
    if not ok:
        print("Connessione chiusa")
    else:
        while True:
            scelta = input("Vuoi inserire un nuovo dato anagrafico o visualizzare quelli inseriti? (i/v): ").lower()
            if scelta == "i":
                messaggio = inserisci_dato_anagrafico()
                invio_messaggio(messaggio, client)
            elif scelta == "v":
                invio_messaggio("visualizza", client)
                risposta = lettura_messaggio(client)
                dati_anagrafici = json.loads(risposta)
                print("Dati anagrafici nel server:")
                for dato in dati_anagrafici:
                    print(dato)
            elif scelta == 'chiudi':
                print("Chiudo la connessione...")
                break
            else:
                print("Scelta non valida, riprova.")

    print("Arrivederci...")
    client.shutdown(socket.SHUT_RDWR)
    client.close()

if __name__ == "__main__":
    main()
