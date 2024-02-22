import socket
from invio_ricezione import lettura_messaggio, invio_messaggio


def main():
	'''
	Il server accetta una connessione dal client.
	
	'''
	server = socket.socket()
	server.bind(("", 8000))
	server.listen()
	print("Listening...")

	while True:
		print("Waiting for connection")
		client1_conn, client1_addr = server.accept()
		print(f"Client {client1_addr[0]} connected on port {client1_addr[1]}")
				
		client1_conn.send("ok".encode())
				
		#Scambio dati
		while True:
			#Leggo un messaggio dal client
			msg = lettura_messaggio(client1_conn)
			print(f"Client: {msg}")
			if msg is None:
				print("Client ha chiuso")
				break
			
			invio_messaggio(msg, client1_conn)

		client1_conn.close()

if __name__ == "__main__":
	main()