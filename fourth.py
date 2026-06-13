import numpy as np
def studentsPerform(marks):
    averages = np.mean(marks, axis=1)
    return np.where(averages > 75)[0].tolist()