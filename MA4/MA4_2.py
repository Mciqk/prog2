#!/usr/bin/env python3

from person import Person

import random
import math
import matplotlib.pyplot as plt
from math import pi, gamma
from numba import jit
import time



#2.0
def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))

@jit(nopython=True)
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return fib_numba(n-1) + fib_numba(n-2)
    

if __name__ == "__main__":
    ns = 47 #
    times_py = []
    times_numba = []
    times_cpp = []

    person = Person()

    for n in ns:
        start_time = time.perf_counter()
        fib_py(n)
        end_time = time.perf_counter()
        times_py.append(end_time - start_time)

        start_time = time.perf_counter()
        fib_numba(n)
        end_time = time.perf_counter()
        times_numba.append(end_time - start_time)

        start_time = time.perf_counter()
        person.fib(n)
        end_time = time.perf_counter()
        times_cpp.append(end_time - start_time)

    plt.plot(ns, times_py, label="Python")
    plt.plot(ns, times_numba, label="Numba")
    plt.plot(ns, times_cpp, label="C++")
    plt.legend()
    plt.xlabel("n")
    plt.ylabel("Time (s)")
    plt.title("Performance of Fibonacci functions")
    plt.savefig("fib_performance.png")
    plt.show()

