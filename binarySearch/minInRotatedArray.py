def findMin(nums):
        # [3, 4, 5, 6, 1, 2]
        # left at 0
        # right at 5
        # left = 3, right = 2
        # middle is 2, m = 5
        # need to find min
        # L  M  R  
        # 3  5  2
        # if the m greater than left and left is more than right
        # we move left to be m + 1
        # store min, compare previoius min, m, r 
        
        # [4,5,6,7]
        # L  M  R  
        # 4  5  7
        # if the m greater than left and left is less than right
        # we move right to be m - 1
        # store new min with args of previous min, l, m 

        # [4,5,0,1,2,3]
        # l = 0 r = 5
        # m = 2
        # L  M  R  
        # 4  0  3
        # if m is less than left and right, move right to m - 1
        # update new min out of m and r options and previous min

        l = 0
        r = len(nums) - 1
        minimum = min(nums[l], nums[r])

        while l <= r:
            m = (l + r) // 2

            if nums[m] > nums[l] and nums[l] > nums[r]:
                l = m + 1
                minimum = min(minimum, nums[r],nums[m])
            elif nums[m] > nums[l] and nums[l] < nums[r]:
                r = m - 1
                minimum = min(minimum, nums[l], nums[m])
            elif nums[m] < nums[l] and nums[m] <  nums[r]:
                r  = m - 1
                minimum = min(minimum, nums[r],nums[m])
            else:
                minimum = min(minimum, nums[l],nums[m])
                l  = m + 1

        return minimum

# print(findMin([3,4,5,6,1,2]))
# print(findMin([1]))
print(findMin([5,1,2,3,4]))