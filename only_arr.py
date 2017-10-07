#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Value, Array, Process

def f5(n, a):
    n.value = 3.1415926
    for i in range(len(a)):
        a[i] *= -1

if __name__ == "__main__":
    # 共有メモリ（Value）を作成します.
    num = Value('d', 0.0)
    # 共有メモリ（Array）を作成します.
    arr = Array('i', range(10))
    print arr[:]
    # サブプロセスを作り、実行します.
#    p = Process(target=f5, args=(num, arr))
#    p = Process(target=f5, args=(arr))
#    p.start()
#    p.join()
    for i in range(len(arr)):
        arr[i] *= -1
    # 共有メモリ（Value）から値を取り出します
    print(num.value)
    # 共有メモリ（Array）から値を取り出します
    print(arr[:])
