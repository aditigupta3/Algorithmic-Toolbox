# Uses python3
import sys


def gcd_naive(a, b):
    """
    Using the lemma taught in lectures GCD(a, b) = GCD(b, rem) if rem is the remainder we get on dividing a by b
    :param a:
    :param b:
    :return:
    """
    if a < b:
        return gcd_naive(b, a)
    elif b == 0:
        return a
    else:
        rem = a % b
        if rem > b:
            return gcd_naive(rem, b)
        else:
            return gcd_naive(b, rem)


def lcm_naive(a, b):
    """
    Using the lemma: a*b = LCM(a, b)*GCD(a,b)
    :param a:
    :param b:
    :return:
    """
    gcd = gcd_naive(a, b)
    # Instead of doing (a*b)/gcd, we do a*(b/gcd) to prevent overflow
    return a*int(b/gcd)


if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

