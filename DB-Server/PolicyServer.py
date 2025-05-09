import socket
import threading

policy_response = b"""<?xml version="1.0"?>
<!DOCTYPE cross-domain-policy 
         SYSTEM "http://www.adobe.com/xml/dtds/cross-domain-policy.dtd">
<cross-domain-policy>
  <allow-access-from domain="*" to-ports="443"/>
</cross-domain-policy>\0"""

def serve_policy():
    try:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("", 843))
        s.listen(5)
        print("Policy server listening on port 843")
        while True:
            conn, addr = s.accept()
            data = conn.recv(1024)
            if b"<policy-file-request/>" in data:
                conn.sendall(policy_response)
            conn.close()
    except Exception as e:
        print(f"Policy server failed: {e}")

t = threading.Thread(target=serve_policy)
t.start()
