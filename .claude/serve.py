import os, http.server, socketserver

PORT = 3000
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

os.chdir(DIR)
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
