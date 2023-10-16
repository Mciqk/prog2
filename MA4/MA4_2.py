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
    
n_values = list(range(30, 46))
#n_values = list(range(20, 31))
#n_values = 47  no pure python
times_py = []
times_numba = []
times_cpp = []

for n in n_values:
    # Timing for fib_py
    start = time.perf_counter()
    fib_py(n)
    end = time.perf_counter()
    times_py.append(end - start)

    # Timing for fib_numba
    start = time.perf_counter()
    fib_numba(n)
    end = time.perf_counter()
    times_numba.append(end - start)

    # Timing for C++ implementation
    person = Person(n)
    start = time.perf_counter()
    person.fib()
    end = time.perf_counter()
    times_cpp.append(end - start)

plt.figure(figsize=(10, 6))
plt.plot(n_values, times_py, '-o', label='fib_py')
plt.plot(n_values, times_numba, '-o', label='fib_numba')
plt.plot(n_values, times_cpp, '-o', label='C++ fib')

plt.xlabel('n')
plt.ylabel('Seconds')
plt.title('Comparison of Fibonacci Implementation Timings')
plt.legend()
plt.grid(True)

# Save the plot to a .png file
plt.savefig('fib_timings.png', bbox_inches='tight')


def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())

if __name__ == "__main__":
    main()
