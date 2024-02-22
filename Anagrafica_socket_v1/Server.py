# Server

import socket
import json
from invio_ricezione import lettura_messaggio, invio_messaggio

def main():
    server = socket.socket()
    server.bind(("", 8000))
    server.listen()
    print("Listening...")

    dati_anagrafici = []

    while True:
        print("Waiting for connection")
        client_conn, client_addr = server.accept()
        print(f"Client {client_addr[0]} connected on port {client_addr[1]}")
                
        client_conn.send("ok".encode())
                
        while True:
            msg = lettura_messaggio(client_conn)
            if msg is None:
                print("Client has closed")
                break

            if msg == "visualizza":
                invio_messaggio(json.dumps(dati_anagrafici), client_conn)
            else:
                try:
                    nuovo_dato_anagrafico = json.loads(msg)
                    dati_anagrafici.append(nuovo_dato_anagrafico)
                except json.JSONDecodeError:
                    print("Errore nel formato del messaggio JSON")

        client_conn.close()

if __name__ == "__main__":
    main()
