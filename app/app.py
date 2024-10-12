from datetime import datetime
from app.config import Config
from app.artist import Artist
from app.database import Database
from ping3 import ping
from time import sleep
import os

class Application():
    def __init__(self):
        self.config = Config('config.json')
        self.artist = Artist()
        self.database = Database()
        pass

    def workloop(self):
        for host in self.config.hosts:
            delay = self.ping(host)
            timestamp = int(datetime.now().timestamp())
            #print(f'{timestamp}: ping {host} = {delay}')
            data = {'host': host, 'timestamp': timestamp, 'delay': delay}
            self.database.push(data)
        pass

    def run(self):
        #self.artist.run()
        for _ in range(999):
            self.workloop()
            sleep(3)
        pass

    def ping(self, host):
        result = int(ping(host, unit='ms'))
        return result

    def signal_handler(self, signum, frame):
        print('os._exit()')
        self.artist.exit = True
        os._exit(0)