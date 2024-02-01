#Uses python3

import sys
from functools import cmp_to_key

def largest_number(a):
    """
    :param a:
    :return:
    """
    #write your code here
    def compare(val1, val2):
        if val1 + val2 > val2 + val1:
            return 1
        else:
            return -1
    res = ""
    for x in sorted(a, key=cmp_to_key(compare), reverse=True):
        res += x
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))    
