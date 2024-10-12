from app.artist import Artist
import os, signal, traceback, time

artist = Artist()

def signal_handler(signum, frame):
    print('os._exit()')
    artist.exit = True
    os._exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    artist.run()
    time.sleep(100000)

if __name__ == '__main__':
    main()