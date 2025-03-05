import socket
import threading

def handle_client(client_socket, server_host, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((server_host, server_port))

    def forward(source, destination, direction):
        while True:
            try:
                data = source.recv(4096)
                if not data:
                    break
                print(f"[{direction}] {data.hex()}")  # Log raw packet data
                destination.sendall(data)
            except Exception as e:
                print(f"[ERROR] {direction} {e}")
                break

    client_thread = threading.Thread(target=forward, args=(client_socket, server_socket, "CLIENT -> SERVER"))
    server_thread = threading.Thread(target=forward, args=(server_socket, client_socket, "SERVER -> CLIENT"))

    client_thread.start()
    server_thread.start()

    client_thread.join()
    server_thread.join()

    client_socket.close()
    server_socket.close()

def start_proxy(proxy_host, proxy_port, server_host, server_port):
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.bind((proxy_host, proxy_port))
    proxy_socket.listen(5)
    print(f"[INFO] Proxy running on {proxy_host}:{proxy_port}, forwarding to {server_host}:{server_port}")

    while True:
        client_socket, addr = proxy_socket.accept()
        print(f"[INFO] Connection from {addr}")
        threading.Thread(target=handle_client, args=(client_socket, server_host, server_port)).start()

if __name__ == "__main__":
    PROXY_HOST = "127.0.0.1"
    PROXY_PORT = 4444  # Client connects here
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = 443   # Actual game server
    start_proxy(PROXY_HOST, PROXY_PORT, SERVER_HOST, SERVER_PORT)
