import socket
import time
import sys

SEVER_IP = 'localhost'
SERVER_PORT = 8888
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((SEVER_IP, SERVER_PORT))

    while True:

        message = input("")

        if(message == 'qq'):
            client.send(message.encode("utf-8"))
            print(f'message {message} sent.')
            time.sleep(0.5)
            client.close()
            # sys.exit()
            break
        elif(message == ''):
            continue
        else:
            client.send(message.encode("utf-8"))
            print(f'message {message} sent.')

            return_data = client.recv(BUFFER_SIZE)
            print(f'{return_data} returned')