import socket
import threading

# Serve a permissive Flash socket policy that allows connections to all ports
policy_response = b'''<?xml version="1.0"?>
<!DOCTYPE cross-domain-policy SYSTEM "http://www.adobe.com/xml/dtds/cross-domain-policy.dtd">
<cross-domain-policy>
    <!-- Allow any domain to connect to any port -->
    <allow-access-from domain="*" to-ports="1-65535" secure="false"/>
</cross-domain-policy>\0'''


def serve_policy():
    """
    Bind to port 843 and respond to Flash policy-file-request messages.
    Logs each connection and policy request.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("", 843))  # Listen on port 843
        s.listen(5)
        print("[PolicyServer] Listening on port 843...")
        while True:
            conn, addr = s.accept()
            client_ip, client_port = addr
            print(f"[PolicyServer] Connection from {client_ip}:{client_port}")
            data = conn.recv(1024)
            if not data:
                print(f"[PolicyServer] No data received from {client_ip}:{client_port}")
            elif b"<policy-file-request/>" in data:
                print(f"[PolicyServer] Policy-file-request received from {client_ip}:{client_port}")
                conn.sendall(policy_response)
                print(f"[PolicyServer] Sent policy response to {client_ip}:{client_port}")
            else:
                print(f"[PolicyServer] Received unexpected data from {client_ip}:{client_port}: {data}")
            conn.close()
    except Exception as e:
        print(f"[PolicyServer] Server failed: {e}")


if __name__ == "__main__":
    t = threading.Thread(target=serve_policy)
    t.daemon = True
    t.start()
    t.join()  # Keep the main thread alive

    while True:
        pass
