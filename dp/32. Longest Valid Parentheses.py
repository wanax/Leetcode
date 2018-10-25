'''
Xiaochi Ma
2018-10-21
'''

class Solution:
    def longestValidParentheses(self, s):
        
        dp = [0 for i in range(len(s))]
        
        for i in range(1, len(s)):
            if s[i] == ')' and s[i-1] == '(':
                if i - 2 >= 0:
                    dp[i] = dp[i-2] + 2
                else:
                    dp[i] = 2
            elif s[i] == ')' and s[i-1] == ')':
                if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2
            
        maxLen = 0
        for n in dp:
            if n > maxLen:
                maxLen = n
        
        return maxLen


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.longestValidParentheses(")()())"))























