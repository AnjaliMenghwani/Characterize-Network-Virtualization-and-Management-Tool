# Characterize-Network-Virtualization-and-Management-Tool
CS 553 Internet Services Final Project

Steps to install Zerotier Client:


1. Install zerotier in the local device or EC2 instance using the command 
curl -s https://install.zerotier.com | sudo bash 

2. Create a 16-digit network ID for the system to connect to Zerotier use the following link https://my.zerotier.com/network/93afae5963b55e77 and navigate to the networks tab

3. Click on the Create A network button and zerotier will generate a 16-digit network ID.

4. Joining the network from the local system or EC2 can be done through the terminal and Zerotier UI.

5. The command mentioned below is used to join a network through the terminal.

sudo zerotier-cli join <networkID>

6. Under the networks section, navigate to the members tab to look at the list of systems that joined the network.
 
7. Using the UI click on the Join New Network option to connect to the respective network.
  
Server: 
  
Initialize the server: The server is initialized by creating a socket, binding it to a specific address and port, and starting to listen for incoming connections.

Accept incoming connection: When a client initiates a connection, the server accepts the incoming connection using ssl_socket.accept(). This call blocks until a client establishes a connection.

Handle client request: Once a connection is established, the server receives the client's request by calling conn.recv(1024). The received data is processed or used to generate a response.

Measure latency: Before sending the response, the server records the start time using time.time(). After sending the response with conn.sendall(), it calculates the end time and calculates the latency as the difference between the start and end times.

Print received data and latency: The server prints the received data and the calculated latency. This provides visibility into the request payload and the time taken to process and respond to the request.
  
Continue handling requests: After processing a client request and measuring the latency, the server continues to listen for new requests from the client in a loop. It repeats steps 3 to 5 for each incoming request.

Close connection: If the client terminates the connection or no more data is received, the server closes the connection using conn.close(). It then waits for a new client connection.

This methodology allows the server to handle incoming requests sequentially, measure the latency for each request, and provide information about the received data and response time. It can be extended or customized based on specific requirements and additional functionality needed in the server application.


