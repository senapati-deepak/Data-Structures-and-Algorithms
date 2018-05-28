# Uses python3
import sys
import numpy as np

def get_optimal_value(W, weights, values):
    value = 0.
    # write your code here

    weights = np.array(weights)
    values = np.array(values)
    vw = values/weights
    values = [v for _,v in sorted(zip(vw,values), reverse= True)]
    weights = [v for _,v in sorted(zip(vw,weights), reverse= True)]
    vw = sorted(vw, reverse= True)
    i=0
    while W != 0 and i<len(vw):
        a = min(weights[i],W)
        value = value + a*(vw[i])
        W = W - a
        i= i+1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
