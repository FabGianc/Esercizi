import socket
from invio_ricezione import lettura_messaggio, invio_messaggio


def main():
	addr = "127.0.0.1"
	port = 8000

	client = socket.socket()

	client.connect((addr, port))

	print("Invia messaggi testuali! (a chi?). Inserisci 'chiudi' per terminare.")
	print("aspetto un interlocutore...")
	ok = client.recv(2)
	if not ok:
		print("Connessione chiusa")
		
	else:
		#Scambio dati
		messaggio : str = ""
		while messaggio != "chiudi":
			messaggio : str = input("Inserisci un messaggio da inviare: ")
			if messaggio == "":
				messaggio = " " #Questo serve per evitare di inviare stringhe vuote che chiudono la connessione
			invio_messaggio(messaggio, client)

			msg = lettura_messaggio(client)
			if msg is None:
				print("Interlocutore disconnesso")
				break
			print(f"Risposta: {msg}")


	print("Arrivederci...")
	client.shutdown(socket.SHUT_RDWR)
	client.close()


if __name__ == "__main__":
	main()