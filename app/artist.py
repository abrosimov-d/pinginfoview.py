import threading, time, signal, os, datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import base64
import gc


class Artist():
    def __init__(self):
        self.exit = False
        self.directory = f'database'
        pass

    def workloop(self):
        hosts = os.listdir(self.directory)
        print({os.path.sep})
        for host in hosts:
            fig, axs = plt.subplots(1, 1, figsize=(12, 3))
            filename = f'{self.directory}{os.path.sep}{host}'
            print('filename', filename)
            lines = self.read_all_lines(filename)
            timestamps = []
            delays = []
            for line in lines[-200:]:
                data = line.strip().split(';')
                timestamp = datetime.datetime.fromtimestamp(int(data[0]))
                delay = int(data[1])
                timestamps.append(timestamp)
                delays.append(delay)

            min_delay = min(delays)
            max_delay = max(delays)
            average = int(sum(delays) / len(delays))

            legend = f'host:{host}\ntime:{str(datetime.datetime.now()).split('.')[0]}\nmin:{min_delay} max:{max_delay} avg:{average}'

            sns.lineplot(x = timestamps, y = delays)
            savefilename = f'images{os.path.sep}{base64.b64encode(host.encode('utf-8')).decode()}.png'
            plt.legend(title=legend, loc='upper left')
            plt.savefig(savefilename)
            plt.clf()
            plt.close('all')  
            gc.collect()

        plt.close()

    def workthread(self):
        while not self.exit:
            gc.enable()
            try:
                self.workloop()
            except Exception as e:
                print('error', e)
            time.sleep(5)
        pass

    def run(self):
        self.thread = threading.Thread(target=self.workthread)
        self.thread.start()
        pass

    def read_all_lines(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                file.close()
                return lines
        except Exception as e:
            print('error: {e}')
            return []