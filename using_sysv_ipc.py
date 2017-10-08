#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sysv_ipc

#use ps aux |grep talk
mem_key = 4894

memory = sysv_ipc.SharedMemory(mem_key)
for i in len(xrange(10)):
      memory_value = memory.read()
      print memory_value
memory.detach()
