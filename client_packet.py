import ssl
import time
import socket

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

        num_packets = 10  # Number of packets to send

        for i in range(num_packets):
            # Create a payload
            packet_number = str(i + 1)
            payload = b'Packet ' + packet_number.encode('utf-8')

            try:
                # Send the payload and record the start time
                start_time = time.time()
                ssl_socket.sendall(payload)

                # Receive the response
                response = ssl_socket.recv(1024)

                # Calculate the end time and latency
                end_time = time.time()
                latency = end_time - start_time

                print("Received data:", response.decode())
                print("Latency: {:.3f} seconds".format(latency))
                print()

            except BrokenPipeError:
                print("Connection with the server was unexpectedly closed.")
                break

            # Wait for a short interval between packets
            time.sleep(0.5)

