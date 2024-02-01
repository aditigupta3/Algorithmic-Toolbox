# Uses python3
import sys
import itertools

def can_partition(nums, k, target, current_sum, start, used):
    if k == 1:
        # This means that we were able to form 2 partitions that sum to target.
        # Implying the third partition will sum to target as well.
        return True

    if current_sum == target:
        # One partition that sums exactly to target has been found.
        # We need to look for the next one
        return can_partition(nums, k - 1, target, 0, 0, used)

    for i in range(start, len(nums)):
        if not used[i] and current_sum + nums[i] <= target:
            used[i] = True
            # If we can create sucessful partitions by putting this element into the current partition
            if can_partition(nums, k, target, current_sum + nums[i], i + 1, used):
                return True
            used[i] = False

    return False

def partition3(nums):
    total_sum = sum(nums)
    if total_sum % 3 != 0:
        return 0
    
    target = total_sum // 3
    k = 3
    current_sum = 0
    start = 0
    used = [False] * len(nums)
    if can_partition(nums, k, target, current_sum, start, used):
        return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

