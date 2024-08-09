import socket

def start_udp_server(host='127.0.0.1', port=65432):
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"UDP server listening on {host}:{port}")

        while True:
            data, addr = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
            print(f"Received message from {addr}: {data.decode()}")
            server_socket.sendto(data, addr)  # Echo the received message back to the client

if __name__ == "__main__":
    start_udp_server()
