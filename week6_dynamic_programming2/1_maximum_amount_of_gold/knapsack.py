# Uses python3
import sys


def optimal_weight(W, w):
    """
    This is a knapsack without repetitions problem.
    :param W:
    :param w:
    :return:
    """
    # write your code here
    max_val = [[0 for j in range(W+1)]]
    for i, v_i in enumerate(w):
        max_val.append(list())
        for j in range(W+1):
            max_ = 0
            if j >= v_i:
                max_ = max_val[i][j - v_i] + v_i
            max_ = max(max_val[i][j], max_)
            max_val[-1].append(max_)
    return max_val[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
