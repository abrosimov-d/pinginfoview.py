from app.app import Application
import os, signal, traceback



def main():
    app = Application()
    signal.signal(signal.SIGINT, app.signal_handler)
    try:
        app.run()
    except Exception as e:
        app.artist.exit = True
        traceback.print_exc()

if __name__ == '__main__':
    main()
