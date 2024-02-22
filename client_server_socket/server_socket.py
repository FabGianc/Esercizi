"""
operazioni sulle socket

lato server
• bind, lega la socket ad una porta
• listen, mette il server in ascolto sulla porta precedentemente scelta
• accept, attende che arrivi una connessione da un client
• send/recv, come nel client
"""

import socket

def main():
    server = socket.socket()
    server.bind(("", 8000))
    server.listen()
    server.settimeout(60) # Imposto in timeout di 60 secondi lato server
    print("Listening...")

    while True:
        print("Waiting for connection...")
        try:
            client_conn, client_addr = server.accept()
            client_conn.settimeout(60)  # Imposto in timeout di 60 secondi lato client

            print(f"Client {client_addr[0]} connected on port {client_addr[1]}")

            # Scambio dati
            somma = 0
            while True:
                data = client_conn.recv(4)
                if not data:
                    print("Client disconnected")
                    break
                numero = int.from_bytes(data, byteorder="big", signed=True)
                print(f"Ricevuto {numero} ")
                somma += numero
                data = somma.to_bytes(4, byteorder="big", signed=True)
                client_conn.send(data)
        
        except socket.timeout:
            print("Timeout: No connection activity. Closing the server...")
            client_conn.close() # Nessuna attività: chiudo il client
            break # Esco dal ciclo e chiudo il server

    server.close()

if __name__ == "__main__":
    main()

