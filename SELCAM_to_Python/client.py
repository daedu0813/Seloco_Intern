import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client: Socket Created')

host = 'localhost'
port = 1233
message = '그만큼 신다신다는거지'

try:
    print('Client: ' + message)
    client_socket.sendto(message.encode(), (host, 1234))

    data, server = client_socket.recvfrom(4096)
    data = data.decode()
    print('Client: ' + data)

finally:
    print('Client: Closing Socket')
    client_socket.close()