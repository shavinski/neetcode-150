def search(nums, target):
    # find target number and return index of it
    # if not in array return -1

    # Target = 6
    # [3, 4, 5, 6, 1 ,2]
    #  L     M        R
    #  M > Target AND L < target
    #  move R to be m - 1

    # [6, 1, 2, 3, 4 ,5]
    #  L     M        R

    #

    # M < target AND R < target
    # move L to be m + 1

    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m

        if nums[l] <= nums[m]:
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1

        else:
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1

    return -1


# print(search([3, 4, 5, 6, 1, 2], 1))
# print(search([3, 5, 6, 0, 1, 2], 4))
# print(search([3, 4, 5, 6, 1, 2], 1))
# print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 8, 1, 2, 3], 8))
