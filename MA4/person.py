import ctypes

# Load the shared library
libfib = ctypes.CDLL('./libfibonacci.so')

# Define the argument and return types
libfib.fib.argtypes = [ctypes.c_int]
libfib.fib.restype = ctypes.c_longlong

n = 47
result = libfib.fib(n)
print(f"Fibonacci({n}) = {result}")
