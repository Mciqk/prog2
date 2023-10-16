import random
import math
import matplotlib.pyplot as plt
from functools import reduce
from math import pi, gamma

def generate_points(n):
    points = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(n)]
    return points

def is_inside_circle(point):
    x, y = point
    return x**2 + y**2 <= 1

def estimate_pi(n):
    points = generate_points(n)
    inside_circle = [point for point in points if is_inside_circle(point)]
    nc = len(inside_circle)
    pi_approximation = 4 * nc / n
    
    print(f"Number of points inside the circle: {nc}")
    print(f"Approximation of pi: {pi_approximation}")
    print(f"Built-in value of pi: {math.pi}")
    
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    
    for point in points:
        if is_inside_circle(point):
            ax.plot(point[0], point[1], 'ro')  # red dot for points inside the circle
        else:
            ax.plot(point[0], point[1], 'bo')  # blue dot for points outside the circle
            
    fig.savefig("circle_plot.png")

    return pi_approximation

def main():
    values_of_n = [1000, 10000, 100000]
    
    for n in values_of_n:
        approximation = estimate_pi(n)
        print(f"For n={n}, Approximation of π: {approximation}")
        plt.show()

if __name__ == "__main__":
    main()

'''
Number of points inside the circle: 785
Approximation of pi: 3.14
Built-in value of pi: 3.141592653589793
For n=1000, Approximation of π: 3.14

Number of points inside the circle: 7837
Approximation of pi: 3.1348
Built-in value of pi: 3.141592653589793
For n=10000, Approximation of π: 3.1348

Number of points inside the circle: 78515
Approximation of pi: 3.1406
Built-in value of pi: 3.141592653589793
For n=100000, Approximation of π: 3.1406
'''