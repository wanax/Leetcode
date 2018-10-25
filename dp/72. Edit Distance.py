'''
Xiaochi Ma
2018-10-21
'''

class Solution:
    
    def minDistance(self, word1, word2):
        
        m = len(word1)
        n = len(word2)
        
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = i
        
        for i in range(n+1):
            dp[0][i] = i
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, 
                                   dp[i][j-1]+1,
                                   dp[i-1][j-1]+1)
        return dp[m][n]
    
    def minDistance2(self, word1, word2):
        
        if word1 == word2:
            return 0
        elif len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)
        elif word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            return 1 + min(self.minDistance(word1[1:], word2),
                           self.minDistance(word1, word2[1:]),
                           self.minDistance(word1[1:], word2[1:]))
        

if __name__ == '__main__':
    
    solution = Solution()
    print(solution.minDistance("", "a"))
    



























