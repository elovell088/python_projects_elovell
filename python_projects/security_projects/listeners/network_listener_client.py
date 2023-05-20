#Security projects - Network Listener Client - Used to connect to specified server - Written by: Eric Lovell
import socket

SERVER_HOST = ''  # Server IP or hostname
SERVER_PORT = 443  # Server port

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    
    # Connect to the server
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Send data to server
    data = 'Test..'
    client_socket.sendall(data.encode('utf-8'))

    # Receive data from the server
    received_data = client_socket.recv(1024)
    print(f"Data from server: {received_data.decode('utf-8')}")

    # Close connection
    client_socket.close()