# Uses python3
import sys


def get_change(m):
    """
    This is a knapsack with repetitions problem. The solution here is:
    Num_coins(m) = 1 + min([m-x for x in [1,3,4]])
    :param m:
    :return:
    """
    # write your code here
    coin_count = [0]
    for i in range(1, m+1):
        min_ = i
        for elem in [1, 3, 4]:
            if i >= elem:
                min_ = min(min_, coin_count[i-elem])
        coin_count.append(min_ + 1)
    return coin_count[-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
