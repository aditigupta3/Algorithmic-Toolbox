# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    """
    Using the fact - for any integers a and b, (a + b) % 10 = (a%10 + b%10)%10
    :param n:
    :return:
    """
    if n <= 1:
        return n

    previous = 0
    current = 1
    for _ in range(n - 1):
        # print(previous, current)
        previous, current = current, (previous + current) % 10

    return current


if __name__ == '__main__':
    input = input()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
