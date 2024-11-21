import math


def search(nums, target):
    # will always need sorted array for binary search
    # have a left pointer, right pointer and middle
    # if middle number is less than target
    # then we move the left pointer to be middle + 1
    # if middle number is more than target
    # we move right pointer to be middle - 1

    l = 0
    r = len(nums) - 1

    while l <= r:
        m = math.floor((l + r) / 2)

        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1

    return False


print(search([-1, 0, 2, 4, 6, 8], 4))
