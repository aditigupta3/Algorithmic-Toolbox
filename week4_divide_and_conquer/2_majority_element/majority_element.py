# Uses python3
import sys


def get_majority_element_helper(a, left, right):
    """
    Using divide and conquer algorithm to find the majority element in an array
    :param a: input list
    :param left: starting index for subarray to find the majority element
    :param right: last index for subarray to find the majority element
    :return idx: index of the majority element in subarray a[left:right]
    :return count: count of the majority element in subarray a[left:right]
    """
    if left == right: # Empty array case
        return -1, 0
    elif left + 1 == right: # Array with 1 element
        return left, 1

    mid = int((left + right) / 2)
    left_majority, l_count = get_majority_element_helper(a, left, mid)
    right_majority, r_count = get_majority_element_helper(a, mid, right)
    if left_majority != -1 and right_majority != -1 and a[left_majority] == a[right_majority]:
        # Majority elements in left and right sub array match
        return left_majority, l_count+r_count
    elif r_count > l_count:
        # The count of majority element is higher in the right sub array
        c = 0
        for elem in a[left:mid]:
            if elem == a[right_majority]:
                c += 1
        if r_count + c > (right-left)//2:
            return right_majority, r_count + c
        else:
            return -1, 0
    elif r_count < l_count:
        # The count of majority element is higher in the left sub array
        c = 0
        for elem in a[mid:right]:
            if elem == a[left_majority]:
                c += 1
        if l_count + c > (right-left)//2:
            return left_majority, l_count + c
        else:
            return -1, 0
    return -1, 0


def get_majority_element(a, left, right):
    idx, _ = get_majority_element_helper(a, left, right)
    if idx == -1:
        return 0
    else:
        return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a, 0, n))