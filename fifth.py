import numpy as np
def anomalousServers(traffic):
    serverAvg = np.mean(traffic, axis=1)
    overallAvg = np.mean(traffic)
    return np.where(serverAvg > 2 * overallAvg)[0].tolist()