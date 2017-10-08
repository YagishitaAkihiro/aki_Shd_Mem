#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import current_process, Process
from random import randrange
import time

def worker(timer):
    p = current_process()
    counter = timer
    while counter >= 0:
          print('%s(PID %s): counter=%d' % (p.name, p.pid, counter))
          counter -= 1
          time.sleep(0.5)

processes = []

for i in range(5):
    timer = randrange(20)
    p = Process(target=worker, args=(timer,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()
