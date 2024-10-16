import datetime

class Logger():
    def __init__(self, filename):
        self.filename = filename
    def debug(self, string):
        timestamp = str(datetime.datetime.now()).split('.')[0]
        self.append_string_to_file(self.filename, f'{timestamp}: {string}')

    def append_string_to_file(self, filename, string):
        try:
            with open(filename, 'a') as file:
                file.write(string + '\n')
        except Exception as e:
            print(f"error: {e}")
        pass