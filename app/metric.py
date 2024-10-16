from app.message import Message


class Metric():
    def __init__(self, host):
        self.host = host
        self.state = 0
        self.status = 'offline'
    
    def process(self, new_sate):
        result = None
        match self.status:
            case 'online':
                if new_sate == -1:
                    self.status = 'offline'
                    self.state = new_sate
                    message = Message()
                    text = f'host {self.host} changed status to {self.status}'
                    message.show('warning', text)
                    result = text

            case 'offline':
                if new_sate > -1:
                    self.status = 'online'
                    self.state = new_sate
                    message = Message()
                    text =  f'host {self.host} changed status to {self.status}'
                    message.show('warning', text)
                    result = text

            case _:
                pass
        return result