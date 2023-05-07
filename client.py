import certifi
import socket
import certifi
import socket
import ssl
import time

HOST = '192.168.192.113'  # Replace with server IP address
PORT = 8443

# Load SSL certificate and private key
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_cert_chain('client.crt', 'client.key')

# Disable certificate validation and hostname checking
context.check_hostname = False

# Set the trusted CA certificates
context.load_verify_locations('ca.crt')

# Create socket and wrap in SSL
with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssl_socket:
        print("Connected to {}:{}".format(HOST, PORT))
        start_time = time.time()
        ssl_socket.sendall(b'Ping')
        data = ssl_socket.recv(1024)
        end_time = time.time()
        print("Received data: ", data.decode())
        print("Latency: {:.3f} seconds".format(end_time - start_time))

