#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Value, Array, Process

def f(a):
    for i in range(len(a)):
        a[i] *= -1

if __name__ == "__main__":
    # 共有メモリ（Array）を作成します.
    arr = Array('i', range(10))
    print arr[:]
    # サブプロセスを作り、実行します.
    p = Process(target=f, args=(arr))
    p.start()
    p.join()
    # 共有メモリ（Array）から値を取り出します
    print(arr[:])
