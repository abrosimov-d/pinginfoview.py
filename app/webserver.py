import http.server
import socketserver
import threading

PORT = 8000
DIRECTORY = "."

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


class Webserver():
    def __init__(self):
        pass

    def workthread(self):
        with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
            print("Serving at port", PORT)
            httpd.serve_forever()

    def run(self):
        self.thread = threading.Thread(target=self.workthread)
        self.thread.start()        
