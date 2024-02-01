# Uses python3
import sys


def optimal_summands(n):
    """
    The maximum number would be possible in case all candies are distributed like this:
    1, 2, 3 and so on. If there are any extras, give them to the top competitor.
    :param n:
    :return:
    """
    # write your code here
    summands = []
    sum_ = 0
    next_ = 1
    while sum_ + next_ <= n:
        summands.append(next_)
        sum_ += next_
        next_ += 1
    left = n-sum_
    if left > 0:
        summands[-1] += left
    return summands


if __name__ == '__main__':
    input = input()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
