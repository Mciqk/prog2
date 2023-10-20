#!/usr/bin/env python3
"""
Student: Boya Lin
Mail: boya.lin.0976@student.uu.se
Reviewed by: William 
Date:
"""
from person import Person
import os
import matplotlib.pyplot as plt
from numba import jit
import time

user_home = os.path.expanduser("~")
save_path = "./"

os.makedirs(os.path.dirname(save_path), exist_ok=True)

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

def cal_time(n_values, function):
    times = []

    for n in n_values:
        start_time = time.perf_counter()  
        function(n)  
        end_time = time.perf_counter()  
        times.append(end_time - start_time)  

    return times   

def plot_times(n_values, py_times, numba_times, cpp_times):
    plt.plot(n_values, py_times, label='Python', color='b')  
    plt.plot(n_values, numba_times, label='Numba', color='g')
    plt.plot(n_values, cpp_times, label='C++', color='r')  
    plt.xlabel('n')  
    plt.ylabel('seconds')
    plt.title('Time for Fibonacci Calculations')
    plt.legend()  

    plt.savefig(save_path)

if __name__ == "__main__":
    n_values = list(range(20, 31))

    py_times = cal_time(n_values, fib_py)  
    numba_times = cal_time(n_values, fib_numba)
    cpp_times = []  

    def cpp_fib(n):
        return Person(n).fib()

    for n in n_values:
        start_time = time.perf_counter()
        cpp_times.append(cal_time([n], cpp_fib)[0])
        end_time = time.perf_counter()  

    plot_times(n_values, py_times, numba_times, cpp_times)  

    n = 47
    print(f"Fibonacci of n={n} with different programming languages:")
    print(f"    Python + Numba: {fib_numba(n)}")
    cpp_result = Person(n).fib()
    print(f"    C++: {cpp_result}")

    print(save_path)

""" Fibonacci of n=47 with different programming languages:
    Python + Numba: 
    C++: 
"""
