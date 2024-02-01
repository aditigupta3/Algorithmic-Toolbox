# Uses python3
def calc_fib(n):
    """
    Iterative solution instead of a recursive one.
    :param n:
    :return:
    """
    if (n <= 1):
        return n
    n_1 = 1
    n_2 = 0
    for i in range(n-1):
        n_1, n_2 = n_1 + n_2, n_1
    return n_1


n = int(input())
print(calc_fib(n))
