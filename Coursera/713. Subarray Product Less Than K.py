'''
Xiaochi Ma
2018-12-18
'''
from functools import reduce
class Solution(object):
    
    def numSubarrayProductLessThanK(self, nums, k):
        
        if k <= 1:
            return 0
        
        l, count, pro = 0, 0, 1
        for r, val in enumerate(nums):
            pro *= val
            while pro >= k:
                pro /= nums[l]
                l += 1
            count += (r - l + 1)
        
        return count
    
    def isPa(self, s):
        return s == s[::-1]
    
    def countSubstrings(self, s):
        
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                
        for i in range(len(s)-3, -1, -1):
            for j in range(i+2, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
        
        return sum(list(map(lambda x:sum(x), dp)))
    
    def minMoves(self, nums):
        
        nums.sort()
        c = 0
        for i in range(len(nums)-1, 0, -1):
            c += (nums[i]-nums[0])
        
        return c
    
    def numMusicPlaylists(self, N, L, K):
        
        mod = 10**9 + 7
        dp = [[0 for i in range(N+1)] for j in range(L+1)]
        dp[0][0] = 1
        
        for i in range(1, L+1):
            for j in range(1, N+1):
                dp[i][j] = (dp[i-1][j-1] * (N-(j-1)))%mod
                if j > K:
                    dp[i][j] = (dp[i][j] + (dp[i-1][j]*(j-K))%mod)%mod
        
        return dp[L][N]
    
    def makeLargestSpecial(self, S):
        
        count, i = 0, 0
        res = []
        for j, v in enumerate(S):
            count += 1 if v == '1' else -1
            if count == 0:
                res.append("1"+self.makeLargestSpecial(S[i+1:j])+"0")
                i = j + 1
        
        return "".join(sorted(res)[::-1])
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.makeLargestSpecial("11011000"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    