# Uses python3
import sys


def optimal_sequence(n):
    """
    Similar to the change problem, this problem can be solutioned as a 1D DP problem.
    min_ops[n] = min(min_ops[n-1], min_ops[n//2], min_ops[n//3]).
    The order of operations can be obtained using backtracking.
    :param n:
    :return:
    """
    if n == 1:
        return [1]
    min_ops = [(0, 0)]
    for i in range(2, n+1):
        min_ = (min_ops[i-2][0] + 1, 0)
        if i % 2 == 0:
            ops = 1 + min_ops[int(i/2) - 1][0]
            if ops < min_[0]:
                min_ = (ops, 1)
        if i % 3 == 0:
            ops = 1 + min_ops[int(i/3) - 1][0]
            if ops < min_[0]:
                min_ = (ops, 2)
        min_ops.append(min_)
    sequence = list()
    while n >= 1:
        sequence.append(n)
        if min_ops[n-1][1] == 0:
            n = n-1
        elif min_ops[n-1][1] == 1:
            n = int(n/2)
        else:
            n = int(n/3)
    return reversed(sequence)


input = input()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
