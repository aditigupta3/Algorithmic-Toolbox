# Uses python3
import sys


def get_change(m):
    """
    Using a greedy strategy for change calculation.
    Safe move: For the highest coin denomination left, extract the maximum amount of money that can be drawn using
    the coin of that type.
    :param m:
    :return:
    """
    # write your code here
    num_coins = 0
    if m >= 10:
        num_coins += int(m/10)
        m = m % 10
    if m >= 5:
        num_coins += int(m/5)
        m = m % 5
    if m > 0:
        num_coins += m
    return num_coins


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
