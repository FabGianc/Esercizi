import socket



def main():
	addr = "127.0.0.1"
	port = 8000

	client = socket.socket()

	client.connect((addr, port))

	#Scambio dati
	numero = int(input("Inserisci un numero: "))
	while numero != 0:
		data = numero.to_bytes(4, byteorder="big", signed = True)

		client.send(data)

		data = client.recv(4)
		if not data:
			print("Connessione chiusa...")
			break
		somma = int.from_bytes(data, byteorder="big", signed=True)
		print(f"Somma: {somma}")
		numero = int(input("Inserisci un numero: "))

	print("Arrivederci...")
	client.shutdown(socket.SHUT_RDWR)
	client.close()


if __name__ == "__main__":
	main()