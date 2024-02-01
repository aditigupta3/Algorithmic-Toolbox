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


def fibonacci_sum_naive(n):
    """
    Using the concept of Pisano period - F_n modulo m is a periodic function. If we have m = 10, we can essentially
    have the last digit of all Fibonacci numbers.
    Now to get the sum, index at which n lies. Now, sum_complete_remainder_array is 280, which is divisible by 10.
    So, the answer is sum(rem_array[:rem_idx]) % 10
    :param n:
    :return:
    """

    rem_array = get_fibonacci_period(n, 10)
    length = len(rem_array)
    rem_idx = n % length
    return sum(rem_array[:rem_idx+1]) % 10


if __name__ == '__main__':
    input = input()
    n = int(input)
    print(fibonacci_sum_naive(n))
