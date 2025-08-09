# static_server.py
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

def start_static_server(
    host: str = "127.0.0.1",
    port: int = 80,
    directory: str = "content/localhost"
):
    class _Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)
    httpd = HTTPServer((host, port), _Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    #print(f"[Static] Serving ./{directory} at http://{host}:{port}/")
    return httpd
