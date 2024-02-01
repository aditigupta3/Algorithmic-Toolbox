# Uses python3
from sys import stdin


def get_fibonacci_period(n, m):
    """
    Getting the last digit of fibonacci numbers
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


def fibonacci_sum_squares_naive(n):
    """
    Using the formula: F_0**2 + F_1**2 + F_3**2 ... + F_n**2 = F_n*F_(n+1)
    Also using the concept of Pisano period: F_n modulo m is a periodic series.
    :param n:
    :return:
    """
    if n <= 1:
        return n
    rem_array = get_fibonacci_period(n+1, 10)
    length = len(rem_array)
    return (rem_array[n % length]*rem_array[(n+1) % length]) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))
