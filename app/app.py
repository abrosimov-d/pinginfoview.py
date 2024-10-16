from datetime import datetime
from app.config import Config
from app.artist import Artist
from app.database import Database
from app.host import Host
from app.webserver import Webserver
from app.logger import Logger
from time import sleep
import os

class Application():
    def __init__(self):
        self.config = Config('config.json')
        self.hosts = [Host(ip) for ip in self.config.hosts]
        self.artist = Artist()
        self.database = Database()
        self.webserver = Webserver()
        self.logger = Logger(f'.{os.path.sep}ui{os.path.sep}log.txt')
        pass

    def workloop(self):
        for host in self.hosts:
            delay = host.ping()
            metric_result = host.metric.process(delay)
            if metric_result != None:
                self.logger.debug(metric_result)
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