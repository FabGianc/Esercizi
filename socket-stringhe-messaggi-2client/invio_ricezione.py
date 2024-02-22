import socket


def invio_messaggio(messaggio: str, client : socket.socket):
	'''
	Protocollo di invio:
	- invia prima un intero di 4 byte che rappresenta la lunghezza del messaggio
	- invia subito dopo il messaggio correttamente codificato
	'''
	data : bytes = messaggio.encode() #Converto la stringa in byte
	data_len : int = len(data) #Misuro la lunghezza del messaggio

	len_byte = data_len.to_bytes(4, byteorder="big", signed=False)
	client.send(len_byte)
	client.send(data)


def lettura_messaggio(client : socket.socket) -> str | None :
	'''
	Protocollo di ricezione:
	- leggi 4 byte per sapere la lunghezza del messaggio
	- avvia un ciclo che continua a leggere il buffer finché tutti i byte del messaggio
	non sono stati letti
	'''
	msg_len = client.recv(4)
	if not msg_len:
		return None
	
	bytes_num  = int.from_bytes(msg_len, byteorder="big", signed=True)
	
	data = client.recv(bytes_num)
	#Connessione improvvisamente chiusa?
	if not data:
		return None
	
	bytes_num -= len(data)

	#Continuo a leggere finché il numero di byte rimasti da leggere non è zero
	while bytes_num > 0:
		data = client.recv(bytes_num)
		#Connessione improvvisamente chiusa?
		if not data:
			return None
		
		bytes_num -= len(data)
	
	return data.decode()
