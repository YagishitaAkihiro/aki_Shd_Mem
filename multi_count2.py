import multiprocessing
import random
import time

class Worker(multiprocessing.Process):
    def __init__(self, timer):
        super(Worker, self).__init__()
        self.timer = timer

    def run(self):
        counter = self.timer
        while counter >= 0:
            print('%s(PID %s): counter=%d' % (self.name, self.pid, counter))
            counter -= 1
            time.sleep(0.5)

processes = []
for i in range(5):
    timer = random.randrange(20)
    p = Worker(timer)
    processes.append(p)
    p.start()

for p in processes:
    p.join()
