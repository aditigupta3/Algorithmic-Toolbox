# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    """
    Fibonacci numbers modulo m is always a periodic series starting with 0,1.
    :param n:
    :param m:
    :return:
    """
    if n <= 1:
        return n

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

    # period of the modulo series
    period = len(rem_array)
    return rem_array[n % period]


if __name__ == '__main__':
    input = input()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
