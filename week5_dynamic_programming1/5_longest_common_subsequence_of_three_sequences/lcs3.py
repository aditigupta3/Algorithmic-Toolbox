#Uses python3

import sys


def lcs3(a, b, c):
    """
    This problem is very similar to the longest common subsequence problem for 2 strings.
    The only difference here is that instead of the recurrence relationship in 2D, we have one in 3D.
    lcs(i,j,k) =
    if (a[i] == b[j]) and (a[i] == c[k]):
        max(lcs[i-1][j][k], lcs[i][j-1][k], lcs[i][j][k-1],
            lcs[i][j-1][k-1], lcs[i-1][j][k-1], lcs[i-1][j-1][k],
            lcs[i-1][j-1][k-1] + 1)
    else:
        max(lcs[i-1][j][k], lcs[i][j-1][k], lcs[i][j][k-1],
            lcs[i][j-1][k-1], lcs[i-1][j][k-1], lcs[i-1][j-1][k],
            lcs[i-1][j-1][k-1])
    This is the longest common subsequence between strings a[:i], b[:j] and c[:k]
    :param a:
    :param b:
    :param c:
    :return:
    """
    # write your code here
    len1 = len(a)
    len2 = len(b)
    len3 = len(c)
    lcs = list()
    for i in range(len1 + 1):
        l1 = list()
        for j in range(len2 + 1):
            l2 = list()
            for k in range(len3+1):
                l2.append(0)
            l1.append(l2)
        lcs.append(l1)
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            for k in range(1, len3+1):
                dis = max(lcs[i-1][j][k], lcs[i][j-1][k], lcs[i][j][k-1],
                          lcs[i][j-1][k-1], lcs[i-1][j][k-1], lcs[i-1][j-1][k])
                if (a[i-1] == b[j-1]) and (a[i-1] == c[k-1]):
                    dis = max(dis, lcs[i-1][j-1][k-1] + 1)
                else:
                    dis = max(dis, lcs[i-1][j-1][k-1])
                lcs[i][j][k] = dis
    return lcs[-1][-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
