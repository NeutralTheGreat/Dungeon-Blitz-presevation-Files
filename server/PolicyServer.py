# File: policy_server.py

import socket
import threading

_policy = b'''<?xml version="1.0"?>
<!DOCTYPE cross-domain-policy SYSTEM
  "http://www.adobe.com/xml/dtds/cross-domain-policy.dtd">
<cross-domain-policy>
  <allow-access-from domain="*" to-ports="1-65535" secure="false"/>
</cross-domain-policy>\0'''

def start_policy_server(host: str = "127.0.0.1", port: int = 843):
    """
    Launches a daemon thread that listens on (host, port) for Flash
    <policy-file-request/> messages and responds with _policy.
    """
    def _serve():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(5)
        #print(f"[Policy] Listening on {host or '0.0.0.0'}:{port}")
        while True:
            conn, addr = sock.accept()
            data = conn.recv(1024)
            if b"<policy-file-request/>" in data:
                #print(f"[Policy] Request from {addr}, sending policy")
                conn.sendall(_policy)
            conn.close()

    thread = threading.Thread(target=_serve, daemon=True)
    thread.start()
    return thread
