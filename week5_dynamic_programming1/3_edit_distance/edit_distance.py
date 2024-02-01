# Uses python3
def edit_distance(s, t):
    """
    As described in lectures, this can be implemented as a 2D DP problem with the recurrence relation:
    distance(i,j) =
    if s[i] == t[j]:
        min(distance[i-1][j] + 1, distance[i][j-1] + 1, distance[i-1][j-1])
    else:
        min(distance[i-1][j] + 1, distance[i][j-1] + 1, distance[i-1][j-1] + 1)
    This is the edit distance between strings s[:i] and t[:j]
    :param s:
    :param t:
    :return:
    """
    len1 = len(s)
    len2 = len(t)
    distance = [list(range(len2+1))]
    for i in range(1, len1 + 1):
        distance.append([i])
        for j in range(1, len2 + 1):
            if s[i-1] == t[j-1]:
                dis = min(distance[i - 1][j] + 1, distance[i][j - 1] + 1, distance[i - 1][j - 1])
            else:
                dis = min(distance[i - 1][j] + 1, distance[i][j - 1] + 1, distance[i - 1][j - 1] + 1)
            distance[-1].append(dis)
    # write your code here
    return distance[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
