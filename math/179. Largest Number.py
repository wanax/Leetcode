'''
Xiaochi Ma
2018-12-01
'''
import functools
class Solution:
    
    def largestNumber(self, nums):
        
        def fun(x, y):
            return x+y > y+x
        
        nums = sorted(nums, key=functools.cmp_to_key(fun), reverse = True)
        num0 = 0
        for num in nums:
            if num == 0:
                num0 += 1
            else:
                break
        for i in range(num0):
            nums.remove(0)
        if len(nums) == 0:
            return 0
        return "".join(map(str, nums))
    
    def __init__(self):
        self.min = 2**31
    
    def dfs(self, matrix, row, col, cur):
        
        if col < 0 or col > len(matrix[0])-1:
            return
        if row > len(matrix) - 1:
            if row == len(matrix):
                self.min = min(sum(cur), self.min)
            return
        
        cur.append(matrix[row][col]) 
        self.dfs(matrix, row+1, col-1, cur)
        self.dfs(matrix, row+1, col, cur)
        self.dfs(matrix, row+1, col+1, cur)
        
    def cal(self, matrix):
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return '0'
        
        for i in range(len(matrix[0])):
            self.dfs(matrix, 0, i, [])
        
        return self.min
        
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.largestNumber([0,9,8,7,6,5,4,3,2,1]))
#    print(solution.cal([[1,2,3],[4,5,6],[7,8,9]]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
