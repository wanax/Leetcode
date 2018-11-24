'''
Xiaochi Ma
2018-11-22
'''

class Solution:
    
    def getRow(self, rowIndex):
        m = self.generate(rowIndex+1)
        return m[rowIndex]
    
    def generate(self, numRows):
        
        m = []
        for i in range(numRows):
            arr = [0 for j in range(i+1)]
            arr[0] = 1
            arr[-1] = 1
            m.append(arr)
            
        for row in range(1, numRows):
            for col in range(1, len(m[row])-1):
                m[row][col] = m[row-1][col-1] + m[row-1][col]
        
        return m
    
    def __init__(self):
        self.res = 999
    
    def minHeler(self, row, index, res, cur, m):
        
        if row >= len(m):
            self.res = min(sum(cur), self.res)
            return
        if index < 0 or index >= len(m[row]):
            return
        
        cur.append(m[row][index])
        self.minHeler(row+1, index, self.res, cur[:], m)
        self.minHeler(row+1, index+1, self.res, cur[:], m)
    
    def minimumTotal(self, triangle):
        
        if not triangle:
            return 0
        
        dp = [[0 for i in range(len(triangle[-1]))] for j in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                left, right = 999, 999
                if j >= 1:
                    left = dp[i-1][j-1]
                if j < len(triangle[i-1]):
                    right = dp[i-1][j]
                dp[i][j] = triangle[i][j] + min(left, right)
        
        return min(dp[len(triangle)-1])
    
    def maxSubArray(self, nums):
        
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0] if nums[0] > 0 else 0
        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] >= 0 else 0)
        return max(dp)
    
    def maxProfit(self, prices):
        
        if len(prices) == 0:
            return 0
        
        local = [0 for i in range(3)]
        global_s = [0 for i in range(3)]
        
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            for j in range(2, 0, -1):
                local[j] = max(global_s[j-1]+(diff if diff>0 else 0), local[j]+diff)
                global_s[j] = max(local[j], global_s[j])
        
        return global_s[2]
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.maxProfit([3,3,5,0,0,3,1,4])) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    