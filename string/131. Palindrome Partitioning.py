'''
Xiaochi Ma
2018-11-24
'''

class Solution:
    
    def getDP(self, s):
        
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
        return dp
    
    def helper(self, s, res, cur, index, dp):
        
        if index == len(s):
            res.append(cur[:])
            return
            
        for i in range(1, len(s)-index+1):
            ss = s[index:index+i]
            if dp[index][index+i-1]:
                cur.append(ss)
                self.helper(s, res, cur, index+i, dp)
                cur.pop(-1)
    
    def partition(self, s):
        
        res = []
        dp = self.getDP(s)
        self.helper(s, res, [], 0, dp)
        
        return res
    
    def minCut(self, s):
        
        dp = self.getDP(s)
        
        f = [0 for i in range(len(s)+1)]
        for i in range(1, len(s)+1):
            f[i] = 999
            for j in range(i):
                if dp[j][i-1]:
                    f[i] = min(f[i], f[j]+1)
        
        return f[len(s)] - 1
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.minCut("aab"))   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
