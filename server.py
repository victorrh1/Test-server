from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Teste", "abc")
        self.end_headers()
        data = f"""
        <html> 
            <head>
                <title>Server Test</title>
            </head>
            <body>
                <p>Testando o servidor</p>
                <p>Diretório: {self.path}</p>
            </body>
        </html>
        """ .encode()
        self.wfile.write(data)

server = HTTPServer(('localhost', 8000), SimpleHandler)
server.serve_forever()