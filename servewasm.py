from http import server
PORT = 8000
class WasmAwareRequestHandler(server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extensions_map['.wasm'] = 'application/wasm'
httpd = server.HTTPServer(('localhost', PORT), WasmAwareRequestHandler)
print('Starting server on port %d' % PORT)
httpd.serve_forever()
