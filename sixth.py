import numpy as np
def kRiskyUsers(trans, k):
    trans = np.array(trans, dtype=float)
    amount = trans[:, 0]
    spent = trans[:, 1]
    failed = trans[:, 2]

    amountnorm = (amount - amount.min()) / (amount.max() - amount.min())
    timenorm = (spent - spent.min()) / (spent.max() - spent.min())
    failednorm = (failed - failed.min()) / (failed.max() - failed.min())

    riskscore = (
        0.6 * amountnorm +
        0.3 * timenorm +
        0.1 * failednorm
    )


    topk = np.argsort(riskscore)[::-1][:k]

    return topk.tolist()