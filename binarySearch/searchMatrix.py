import math

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        top = 0
        bottom = len(matrix) - 1

        lastEl = len(matrix[0]) - 1

        while top <= bottom:
            m = math.floor((top + bottom) / 2)
        
            if matrix[m][lastEl] < target:
                top = m + 1
            elif matrix[m][0] > target:
                bottom = m - 1
            else:
                break
        
        found = math.floor((top + bottom) / 2)
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            m = math.floor((l + r) / 2)

            if matrix[found][m] == target:
                return True            
            elif matrix[found][l] < target:
                l = m + 1
            elif matrix[found][r] > target:
                r = m - 1
        
        return False

# print(searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15))
print(searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))