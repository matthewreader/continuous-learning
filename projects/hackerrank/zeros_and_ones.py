# You are given the shape of the array in the form of space-separated integers, each integer representing
# the size of different dimensions, your task is to print an array of the given shape and integer type using
# the tools numpy.zeros and numpy.ones.

import numpy as np

if __name__ == "__main__":
    dims = tuple(int(x.strip()) for x in input().split(' '))
    print(np.zeros(dims, dtype=np.int))
    print(np.ones(dims, dtype=np.int))
