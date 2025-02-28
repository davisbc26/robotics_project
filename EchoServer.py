import socket

# SERVER_IP = 'localhost'
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    server.bind((SERVER_IP, SERVER_PORT))
    server.listen(5)
    print('TCP Echo server is listening .... ')

    client_conn, client_addr = server.accept()
    print(f'conneted to {client_addr}')

    while True:
        data = client_conn.recv(1024)
        print(f'received: {data}')

        if(data.decode() == 'qq'):
            server.close()
            break
        elif(data.decode() == ''):
            server.close()
            break
        else:
            client_conn.send(data)