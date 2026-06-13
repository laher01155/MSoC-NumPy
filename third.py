import numpy as np
def maxsumRow(arr):
    return np.argmax(np.sum(arr, axis=1))