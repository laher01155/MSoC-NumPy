import numpy as np
def evenfilter(arr):
    return arr[arr % 2 == 0].tolist()