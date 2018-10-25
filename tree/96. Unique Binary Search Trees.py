'''
Xiaochi Ma
2018-10-21
'''

class Solution:
    def numTrees(self, n):
        
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        
        for i in range(1, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-j-1]
        
        return dp[n]



if __name__ == '__main__':
    
    solution = Solution()
    print(solution.numTrees(3))   


























