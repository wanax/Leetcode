'''
Xiaochi Ma
2018-11-21
'''

class Solution(object):
    
    def numDistinct(self, s, t):
        
        dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
        
        dp[0] = [1 for i in range(len(s)+1)]
        
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        
        return dp[len(t)][len(s)]
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.numDistinct("rabbbit", "rabbit"))  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    