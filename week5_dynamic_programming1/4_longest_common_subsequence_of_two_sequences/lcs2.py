#Uses python3

import sys


def lcs2(a, b):
    """
    This problem is very similar to the edit distance problem. A 2D DP solution can be prepared with the recurrence
    relationship:
    lcs(i,j) =
    if a[i] == b[j]:
        max(lcs[i-1][j], lcs[i][j-1], lcs[i-1][j-1] + 1)
    else:
        max(lcs[i-1][j], lcs[i][j-1], lcs[i-1][j-1])
    This is the longest common subsequence between strings a[:i] and b[:j]
    :param a:
    :param b:
    :return:
    """
    # write your code here
    len1 = len(a)
    len2 = len(b)
    lcs = [[0]*(len2+1)]
    for i in range(1, len1 + 1):
        lcs.append([0])
        for j in range(1, len2 + 1):
            if a[i-1] == b[j-1]:
                dis = max(lcs[i - 1][j], lcs[i][j - 1], lcs[i - 1][j - 1] + 1)
            else:
                dis = max(lcs[i - 1][j], lcs[i][j - 1], lcs[i - 1][j - 1])
            lcs[-1].append(dis)
    # write your code here
    return lcs[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
