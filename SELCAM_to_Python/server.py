import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Server: Socket Created')

host = 'localhost'
port = 1234

server_socket.bind((host, port))
print('Server: Socket Connected to ' + host)

funny_message = ', This is a 무야호!'

while 1:
    data, addr = server_socket.recvfrom(4096)

    if data:
        print('Server: Sending the Funny Message')
        server_socket.sendto(data + (funny_message.encode()), addr)
        