'''
Xiaochi Ma
2018-11-19
'''

class Solution:
    
    def helper(self, s1, m, s2, n, s3, res):
        
        if m == len(s1) and n == len(s2):
            strs = "".join(res)
            if strs == s3:
                return True
            else:
                return False
        
        ans = False
        if m < len(s1):
            res.append(s1[m])
            ans |= self.helper(s1, m+1, s2, n, s3, res)
            res.pop()
        if n < len(s2):
            res.append(s2[n])
            ans |= self.helper(s1, m, s2, n+1, s3, res)
            res.pop()
        
        return ans
            
    
    def isInterleave(self, s1, s2, s3):
        
        if len(s3) != len(s1) + len(s2):
            return False
        
        dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        return True if dp[len(s1)][len(s2)] else False
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.isInterleave("", "", ""))  































