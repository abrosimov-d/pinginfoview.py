from datetime import datetime
from app.config import Config
from app.artist import Artist
from app.database import Database
from app.host import Host
from app.webserver import Webserver
from time import sleep
import os

class Application():
    def __init__(self):
        self.config = Config('config.json')
        self.hosts = [Host(ip) for ip in self.config.hosts]
        self.artist = Artist()
        self.database = Database()
        self.webserver = Webserver()
        pass

    def workloop(self):
        for host in self.hosts:
            delay = host.ping()
            host.metric.process(delay)
            timestamp = int(datetime.now().timestamp())
            #print(f'{timestamp}: ping {host} = {delay}')
            data = {'host': host.ip, 'timestamp': timestamp, 'delay': delay}
            self.database.push(data)
        pass

    def run(self):
        self.artist.run()
        self.webserver.run()
        for _ in range(9999999):
            self.workloop()
            sleep(5)
        pass

    def signal_handler(self, signum, frame):
        print('os._exit()')
        self.artist.exit = True
        os._exit(0)