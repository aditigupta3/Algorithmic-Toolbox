# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    """
    Greedy algorithm with safe move as:
    Select the item with the highest value/weight ratio.
    If you have enough capacity, keep it in full. Otherwise, keep only the fraction that fits.
    :param capacity:
    :param weights:
    :param values:
    :return:
    """
    total_val = 0.
    total_wgt = 0.
    wgt_vals = sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True)
    for wgt, val in wgt_vals:
        if total_wgt + wgt <= capacity:
            total_wgt += wgt
            total_val += val
        else:
            frac = (capacity - total_wgt)/wgt
            total_wgt += frac*wgt
            total_val += frac*val
            break
    # write your code here
    return total_val


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
