# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    """
    As described in the lectures, to get to the maximum value of the expression, we need the maximum and minimum value
    of all possible sub-expressions. The recurrence relationship looks like:
    min_[i][j] = min([min_[i][k] op_k min_[k+1][j], min_[i][k] op_k max_[k+1][j],
                      max_[i][k] op_k min_[k+1][j], max_[i][k] op_k max_[k+1][j]] for all k in the range(i, j))
    max_[i][j] = max([min_[i][k] op_k min_[k+1][j], min_[i][k] op_k max_[k+1][j],
                      max_[i][k] op_k min_[k+1][j], max_[i][k] op_k max_[k+1][j]] for all k in the range(i, j))
    :param dataset:
    :return:
    """
    # Getting the input dataset in the form of list of digits and list of operations
    digits = list()
    ops = list()
    for i, symbol in enumerate(dataset):
        if i % 2 == 0:
            digits.append(int(symbol))
        else:
            ops.append(symbol)
    n = len(digits)

    # Initialising the maximum and minimum 2D matrices to all zeros
    max_ = list()
    min_ = list()
    for i in range(n):
        maxi_ = list()
        mini_ = list()
        for j in range(n):
            maxi_.append(0)
            mini_.append(0)
        max_.append(maxi_)
        min_.append(mini_)

    # Going from difference j - i = 0 to n-1, compute the minimum and maximum possible values of the sub-expression
    for i in range(n):
        max_[i][i] = digits[i]
        min_[i][i] = digits[i]

    for diff in range(1, n):
        for j in range(diff, n):
            i = j - diff
            minij = list()
            maxij = list()
            # i = 0, j = 1, k = 0
            for k in range(i, j):
                minik = min_[i][k]
                minkj = min_[k+1][j]
                maxik = max_[i][k]
                maxkj = max_[k+1][j]
                alevals = [evalt(minik, minkj, ops[k]), evalt(minik, maxkj, ops[k]),
                           evalt(maxik, minkj, ops[k]), evalt(maxik, maxkj, ops[k])]
                minij.append(min(alevals))
                maxij.append(max(alevals))
            min_[i][j] = min(minij)
            max_[i][j] = max(maxij)
    return max_[0][-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
