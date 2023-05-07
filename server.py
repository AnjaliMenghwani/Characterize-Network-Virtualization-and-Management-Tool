import socket
import ssl

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 8443

# Load SSL certificate and private key
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('server.crt', 'server.key')

# Set the trusted CA certificates
context.load_verify_locations('ca.crt')

# Create socket and wrap in SSL
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()

    with context.wrap_socket(sock, server_side=True) as ssl_socket:
        conn, addr = ssl_socket.accept()
        print("Accepted connection from {}:{}".format(addr[0], addr[1]))
        data = conn.recv(1024)
        print("Received data: ", data)
        conn.sendall(b'Hello, World')

