'''
Xiaochi Ma
2018-10-15
'''

class Solution(object):
    def isMatch(self, s, p):
        if len(s) == 0 or len(p) == 0:
            return False
        
        dp = [[False for i in range(len(s) + 1)] for j in range(len(p) + 1)]
        dp[0][0] = True
        
        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                dp[i][0] = dp[i-2][0]
        
        for si in range(1, len(s)+1):
            for pi in range(1, len(p)+1):
                if p[pi-1] == '.' or p[pi-1] == s[si-1]:
                    dp[pi][si] = dp[pi-1][si-1]
                elif p[pi-1] == '*':
                    if p[pi-2] == s[si-1] or p[pi-2] == '.':
                        dp[pi][si] = dp[pi][si-2] or dp[pi-1][si]
                    else:
                        dp[pi][si] = dp[pi][si-2]
        
        return dp[len(p)][len(s)]
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.isMatch('aa', 'a'))
                    

































