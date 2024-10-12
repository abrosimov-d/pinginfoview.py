from datetime import datetime
from app.config import Config
from app.artist import Artist
from ping3 import ping
from time import sleep

class Application():
    def __init__(self):
        self.config = Config('config.json')
        self.artist = Artist()
        pass

    def workloop(self):
        for host in self.config.hosts:
            delay = self.ping(host)
            timestamp = int(datetime.now().timestamp())
            print(f'{timestamp}: ping {host} = {delay}')            
        pass

    def run(self):
        self.artist.run()
        for _ in range(5):
            self.workloop()
            sleep(3)
        pass

    def ping(self, host):
        result = int(ping(host, unit='ms'))
        return result