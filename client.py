import socket
import select
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print ("Print in the following order : script, IP address, port number")
    exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
client_socket.connect((IP_address, Port))

while True:
    sockets_list = [sys.stdin, client_socket]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

    for socks in read_sockets:
        if socks == client_socket:
            message = socks.recv(1024)
            print (message)
        else:
            message = sys.stdin.readline()
            client_socket.send(message.encode('utf-8'))
            sys.stdout.flush()
client_socket.close()
sys.exit()
