# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    """
    Function to get the number of inversions required to sort the array using
    a divide and conquer algorithm.
    """
    def merge(l, m1, m2, r):
        """
        Returns the resulting sorted array when merging the values in sub-arrays l:m1 and m2:r.
        Also returns the number of pairs (b, c) such that b ∈ a[l:m1], c ∈ a[m2:r] and b > c
        """
        new = a[m2:r+1]
        inv = 0
        idx1 = m1
        idx2 = len(new)-1
        for i in range(r, l-1, -1):
            if idx1 >= l and idx2 >= 0:
                if a[idx1] > new[idx2]:
                    a[i] = a[idx1]
                    inv += idx2+1
                    idx1 -= 1
                else:
                    a[i] = new[idx2]
                    idx2 -= 1
            elif idx1 >= l:
                a[i] = a[idx1]
                idx1 -= 1
            else:
                a[i] = new[idx2]
                idx2 -= 1
        return inv
    
    if right - left <= 1:
        return 0
    mid = (left + right) // 2
    # Get the number of inversions required to sort the first half
    inv_left = get_number_of_inversions(a, b, left, mid)
    # Get the number of inversions required to sort the second half
    inv_right = get_number_of_inversions(a, b, mid, right)
    # Get the number of inversions require to merge the 2 halves
    merge_inv = merge(left, mid-1, mid, right-1)
    return inv_left + inv_right + merge_inv

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))

