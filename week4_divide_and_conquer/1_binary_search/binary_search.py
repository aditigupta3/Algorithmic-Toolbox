# Uses python3
import sys


def binary_search(a, x):
    """
    :param a: sorted list
    :param x: element to be searched
    :return:
    """
    left, right = 0, len(a)
    while left < right:
        mid = int((left + right)/2)
        if x == a[mid]: # target is found at the middle position
            return mid
        elif x < a[mid]: # target is smaller than the element at the middle position
            right = mid
        else: # target is larger than the element at the middle position
            left = mid + 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')
