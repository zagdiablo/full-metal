import http.server
import socketserver
from pathlib import Path
import os

from definitions import ROOT_DIR

PORT = 8000
build_folder_path = os.path.join(ROOT_DIR+'/build')

# Custom request handler to serve files from the specified directory
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=build_folder_path, **kwargs)

def serve():
    # Create and start the server
    try:
        with socketserver.TCPServer(("127.0.0.1", PORT), CustomHandler) as httpd:
            print(f"Serving on http://127.0.0.1:{PORT} << Ctrl + Click to see your site.")
            httpd.serve_forever()
    except KeyboardInterrupt:
        quit()
