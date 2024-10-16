from app.metric import Metric
from ping3 import ping

class Host():
    def __init__(self, ip):
        self.ip = ip
        self.metric = Metric(self.ip)
    
    def process(self):
        pass

    def ping(self):
        result = -1
        try:
            result = int(ping(self.ip, unit='ms'))
        except:
            pass
        return result
