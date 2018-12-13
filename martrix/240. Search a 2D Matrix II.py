'''
Xiaochi Ma
2018-12-11
'''

class Solution(object):
    
    def searchMatrix(self, matrix, target):
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        nrow = len(matrix)
        
        res = 0
        l, r = 0, nrow-1
        if target >= matrix[r][0]:
            res = r
        else:
            mid = 0
            while l < r-1:
                mid = (l+r)//2
                if matrix[mid][0] > target:
                    r = mid
                elif matrix[mid][0] < target:
                    l = mid
                else:
                    res = l
                    break
            if matrix[mid][0] == target:
                return True
        
        if res != nrow-1:
            res = l
        for i in range(res+1):
            arr = matrix[i]
            l, r = 0, len(arr)-1
            while l <= r:
                m = (l+r)//2
                if arr[m] > target:
                    r = m-1
                elif arr[m] < target:
                    l = m+1
                else:
                    return True
        return False
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    