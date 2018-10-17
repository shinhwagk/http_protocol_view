from http.server import HTTPServer, BaseHTTPRequestHandler

host = ('localhost', 8888)


class HttpProtocolView(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.headers)

    def do_POST(self):
        data = self.rfile.read(
            int(self.headers['content-length'])).decode('utf-8')
        print(self.headers)
        print(data)


server = HTTPServer(host, HttpProtocolView)
print('http server start, listen %s' % host[1])
server.serve_forever()
