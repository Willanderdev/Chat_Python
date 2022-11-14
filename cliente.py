import socket

HOST = 'localhost'
PORT = 50000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))

servidor.listen()

print('Aguardando resposta...')
cliente, ender = servidor.accept()

print('conectado em', ender)
close = False

while not close:
    data = cliente.recv(1024).decode('utf-8')
    if data == 'exit': 
        close = True
    else:
        print(data)
    cliente.send(input('Mensagem: ').encode('utf-8'))

cliente.close()
servidor.close()


    #  not data:
    #     print('fechando conexão')
    #     conn.close()
    #     break
    # conn.sendall(data)