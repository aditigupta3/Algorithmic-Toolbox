# Uses python3
import sys


def get_fibonacci_period(n, m):
    """
    Getting the last digit of fibonacci numbers.
    :param n:
    :param m:
    :return:
    """
    # computing the array of possible remainders
    previous = 0
    current = 1
    rem_array = [0, 1]
    for _ in range(n - 1):
        previous, current = current, previous + current
        rem_array.append(current % m)
        if (rem_array[-1] == 1) and (rem_array[-2] == 0):
            rem_array.pop(-1)
            rem_array.pop(-1)
            break
    return rem_array


def fibonacci_partial_sum_naive(from_, to):
    """
    Using the concept of Pisano period - F_n modulo m is a periodic function. If we have m = 10, we can essentially
    have the last digit of all Fibonacci numbers.
    Now to get the partial sum, we need to see the index at which to and from lie. 2 cases arise:
    1. index_to >= index_from:
       Final_remainder = (sum(rem_array[idx_from:idx_to+1]) + sum_complete_remainder_array*X) % 10
    2. index_from >= index_to:
       Final_remainder = (sum(rem_array[idx_from:]) + sum(rem_array[:idx_to+1]) + sum_complete_remainder_array*X) % 10
    Now, sum_complete_remainder_array is 280, which is divisible by 10.
    :param from_:
    :param to:
    :return:
    """
    rem_array = get_fibonacci_period(to, 10)
    length = len(rem_array)
    idx_from = from_ % length
    idx_to = to % length
    if idx_to >= idx_from:
        return sum(rem_array[idx_from:idx_to+1]) % 10
    else:
        return sum(rem_array[idx_from:] + rem_array[:idx_to+1]) % 10


if __name__ == '__main__':
    input = input()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))