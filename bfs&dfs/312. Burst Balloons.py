'''
Xiaochi Ma
2018-12-26
'''

class Solution:
    
    def get(self, nums, i):
        if i == -1 or i == len(nums):
            return 1
        return nums[i]
    
    def dfs2(self, mem, nums, s, e):
        
        if s > e:
            return 0
        if s == e:
            return nums[s]
        key = ''.join(str(e) for e in nums[s:e+1])
        if (key in mem):
            return mem[key]
        
        maxp = nums[s]
        for i in range(s, e+1):
            val = self.dfs(mem, nums, s, i-1) +\
            self.get(nums, i) * self.get(nums, s-1) * self.get(nums, e+1) + \
            self.dfs(mem, nums, i+1, e)
            maxp = max(maxp, val)
            
        key = ''.join(str(e) for e in nums[s:e+1])
        mem[key] = maxp
        return maxp
    
    def dfs(self, nums, start, end, dp):
        if start > end:
            return 0
        if dp[start][end] != 0:
            return dp[start][end]
        mm = nums[start]
        for i in range(start, end+1):
            val = self.dfs(nums, start, i-1,dp) + \
            self.get(nums, i) * self.get(nums, start-1) * self.get(nums, end+1) + \
            self.dfs(nums, i+1, end, dp)
            mm = max(mm, val)
        dp[start][end] = mm
        return mm
    
    def maxCoins(self, nums):
        
#        mem = {}
#        res = self.dfs(mem, nums, 0, len(nums)-1)
        
        dp = [[0] * len(nums) for i in range(len(nums))]
        res = self.dfs(nums, 0, len(nums)-1, dp)
        
        return res
    
    def maxCoins2(self, nums):

        N = len(nums)
        nums = [1] + nums + [1]

        f = [[0] * (N + 2) for _ in range(N + 2)]

        for length in range(2, N + 2):
            for i in range(N - length + 2):
                j = i + length
                mij = nums[i] * nums[j]
                for mid in range(i + 1, j):
                    v = f[i][mid] + f[mid][j] + mij * nums[mid]
                    if v > f[i][j]:
                        f[i][j] = v

        return f[0][N + 1]
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.maxCoins2([3,1,5,8])) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    