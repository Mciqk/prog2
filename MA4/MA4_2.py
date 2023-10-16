#!/usr/bin/env python3

from person import Person

import random
import math
import matplotlib.pyplot as plt
from functools import reduce
from math import pi, gamma

#1.1

###############################
#1.2
def monte_carlo_volume(n, d):
    points = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)] #comprehension

    inside_points = filter(lambda p: sum(x**2 for x in p) <= 1, points) #filter() and lambda function

    count_inside = sum(1 for _ in inside_points)

    volume_unit_cube = 2**d
    volume = (count_inside / n) * volume_unit_cube

    return volume

def analytical_volume(d):
    # Volume formula for d-dimensional hypersphere with radius 1
    return (pi ** (d / 2)) / gamma(d / 2 + 1)

n = 100000  # Number of random points
d = 11      # Dimension

# Monte Carlo volume estimation
estimated_volume = monte_carlo_volume(n, d)
print(f"Monte Carlo Estimated Volume (d={d}):", estimated_volume)

# Analytical volume
actual_volume = analytical_volume(d)
print(f"Analytical Volume (d={d}):", actual_volume)



def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())

if __name__ == "__main__":
    main()
