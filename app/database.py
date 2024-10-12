import os

class Database():
    def __init__(self):
        os.makedirs(f'.{os.path.sep}database', exist_ok=True)
        pass

    def push(self, data):
        print(f'db.push() {data}')
        filename = f'.{os.path.sep}database{os.path.sep}{data['host']}'
        line = f'{data['timestamp']};{data['delay']}'
        self.append_string_to_file(filename, line)

    def append_string_to_file(self, filename, string):
        try:
            with open(filename, 'a') as file:
                file.write(string + '\n')
        except Exception as e:
            print(f"error: {e}")
        pass