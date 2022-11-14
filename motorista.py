import socket

HOST = 'localhost'
PORT = 50000

motorista = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
motorista.connect((HOST, PORT))

close = False
while True:
    
    motorista.send(input('Mensagem: ').encode('utf-8'))
    data = motorista.recv(1024).decode('utf-8')
    if data == 'exit':
        close = True
    else:
        print(data)
       
motorista.close()

        

