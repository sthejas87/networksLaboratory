import socket

def start_udp_client(host='127.0.0.1', port=65432):
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        message = "Hello, UDP Server!"
        client_socket.sendto(message.encode(), (host, port))
        
        data, server = client_socket.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    start_udp_client()
