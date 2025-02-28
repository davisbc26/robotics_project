import socket

# SERVER_IP = 'localhost'
SERVER_IP = '10.42.0.1'     # IP of Raspberry Pi
SERVER_PORT = 8888
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    server.bind((SERVER_IP, SERVER_PORT))
    server.listen(5)
    print('TCP Echo server is listening .... ')

    client_conn, client_addr = server.accept()
    print(f'conneted to {client_addr}')

    while True:
        data = client_conn.recv(BUFFER_SIZE)    # buffer size is 1 kB
        print(f'received: {data}')

        if(data.decode() == 'qq'):  # data needs to be decoded from byte to UTF-8 (default for Python)
            server.close()          # return all resources assigned to server to OS
            break
        elif(data.decode() == ''):
            server.close()
            break
        else:
            client_conn.send(data)  # send data back to client