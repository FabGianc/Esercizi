import socket
from invio_ricezione import lettura_messaggio, invio_messaggio



def main():
	'''
	Il server accetta due connessioni da due client diversi (per utilizzare il programma, bisogna lanciare
	due volte lo script client).
	Il server funge da INTERMEDIARIO tra i due client, e inoltra un messaggio del primo client
	all'altro client.
	'''
	server = socket.socket()
	server.bind(("", 8000))
	server.listen()
	print("Listening...")

	while True:
		print("Waiting for connection")
		client1_conn, client1_addr = server.accept()
		print(f"Client C1 {client1_addr[0]} connected on port {client1_addr[1]}")
		
		client2_conn, client2_addr = server.accept()
		print(f"Client C2 {client2_addr[0]} connected on port {client2_addr[1]}")
		
		client1_conn.send("ok".encode())
		client2_conn.send("ok".encode())
		
		#Scambio dati
		while True:
			#Leggo un messaggio dal primo client
			msg = lettura_messaggio(client1_conn)
			print(f"C1: {msg}")
			if msg is None:
				print("C1 ha chiuso")
				break
			
			#Inoltro il messaggio ad un secondo client
			invio_messaggio(msg, client2_conn)
			print("leggo 2")
			msg = lettura_messaggio(client2_conn)

			if msg is None:
				print("C2 ha chiuso")
				break
			invio_messaggio(msg, client1_conn)

		client1_conn.close()
		client2_conn.close()

if __name__ == "__main__":
	main()