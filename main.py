from app.app import Application
import os, signal

def signal_handler(signum, frame):
    print('os._exit()')
    os._exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    app = Application()
    app.run()


if __name__ == '__main__':
    main()
