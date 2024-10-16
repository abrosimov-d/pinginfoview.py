from app.message import Message


class Metric():
    def __init__(self, host):
        self.host = host
        self.state = 0
        self.status = 'offline'
    
    def process(self, new_sate):
        match self.status:
            case 'online':
                if new_sate == -1:
                    self.status = 'offline'
                    self.state = new_sate
                    message = Message()
                    message.show('warning', f'host {self.host} changed status to {self.status}')

            case 'offline':
                if new_sate > -1:
                    self.status = 'online'
                    self.state = new_sate
                    message = Message()
                    message.show('warning', f'host {self.host} changed status to {self.status}')

            case _:
                pass