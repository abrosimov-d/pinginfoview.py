import threading, time, signal, sys

class Artist():
    def __init__(self):
        pass

    def workloop(self):
        print('artist.workloop()')
        pass

    def workthread(self):
        for _ in range(10):
            self.workloop()
            time.sleep(5)
        pass

    def run(self):
        self.thread = threading.Thread(target=self.workthread)
        self.thread.start()
        pass

