'''
Xiaochi Ma
2018-11-16
'''

class Solution:
    
    def setZeroes(self, matrix):
        
        targets = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    targets.append([i, j])
                    
        for item in targets:
            
            row = item[0]
            col = item[1]
            
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
            for i in range(len(matrix)):
                matrix[i][col] = 0
        
        return matrix
    
    def searchMatrix(self, matrix, target):
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        first = []
        for i in range(len(matrix)):
            first.append(matrix[i][0])
        
        l = 0
        while l <= len(first)-1 and first[l] < target:
            l += 1
        if l <= l <= len(first)-1 and first[l] == target:
            return True
        if l > 0:
            l -= 1

        first = matrix[l]
        l, r = 0, len(matrix[l])-1
        while l <= r:
            mid = (l + r)//2
            if first[mid] == target:
                return True
            elif first[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 30)) 
#    print(solution.searchMatrix([[1],[3]], 1)) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    