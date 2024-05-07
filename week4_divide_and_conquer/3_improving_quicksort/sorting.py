# Uses python3
import sys
import random


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def partition3(a, l, r):
    eq_start = l
    eq_end = l+1
    # print(eq_start, eq_end)
    for i in range(l+1, r+1):
        # print(i, eq_start, eq_end, a)
        if a[i] < a[eq_start]:
            # print("Case 1")
            a[i], a[eq_start] = a[eq_start], a[i]
            a[i], a[eq_end] = a[eq_end], a[i]
            eq_start += 1
            eq_end += 1
        elif a[i] == a[eq_start]:
            # print("Case 2")
            a[i], a[eq_end] = a[eq_end], a[i]
            eq_end += 1
    # print(i, eq_start, eq_end, a)
    return eq_start, eq_end

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = l #random.randint(l, r)
    # print("Start:", a, l, r, k, a[k])
    a[l], a[k] = a[k], a[l]
    eq_start, eq_end = partition3(a, l, r)
    # print(a, eq_start, eq_end)
    randomized_quick_sort(a, l, eq_start-1)
    randomized_quick_sort(a, eq_end, r)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
