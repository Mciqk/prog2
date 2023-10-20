import random
from concurrent import futures
import time

def approximate_pi(n, d):
    count_inside_circle = 0
    for _ in range(n):
        x, y = random.uniform(0, d), random.uniform(0, d)
        distance_to_origin = x**2 + y**2
        if distance_to_origin <= d**2:
            count_inside_circle += 1
    return 4 * count_inside_circle / n

def parallel_approximate_pi(n, d, processes):
    with futures.ProcessPoolExecutor(max_workers=processes) as executor:
        future_results = [executor.submit(approximate_pi, n // processes, d) for _ in range(processes)]
        return sum([future.result() for future in future_results]) / processes

if __name__ == '__main__':
    n, d = 10000000, 11

    # Without Parallelization
    start_time = time.perf_counter()
    pi_approximation = approximate_pi(n, d)
    end_time = time.perf_counter()
    print(f"Time Taken (Without Parallelization): {end_time - start_time} seconds")
    #print(f"Approximated Value of Pi: {pi_approximation}")

    # With Parallelization (10 processes)
    start_time = time.perf_counter()
    pi_approximation_parallel = parallel_approximate_pi(n, d, 10)
    end_time = time.perf_counter()
    print(f"Time Taken (With 10 Processes): {end_time - start_time} seconds")
    #print(f"Parallel Approximated Value of Pi: {pi_approximation_parallel}")

#Time Taken (Without Parallelization): 4.620044416980818 seconds
#Time Taken (With 10 Processes): 1.0687178749940358 seconds

#The parallel version with 10 processes is faster than the non-parallel version.

'''
The speedup is due to the parallelized tasks being distributed across multiple CPU cores. 
Each core processes a chunk of data, and by doing so simultaneously, the overall execution time is reduced.
The exact speedup might vary depending on the hardware and system configuration. 
On a system with multiple CPU cores, the parallel version can utilize all available cores, leading 
to a near-linear speedup, especially for compute-bound tasks like this.
'''