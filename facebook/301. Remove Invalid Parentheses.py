'''
Xiaochi Ma
2018-10-31
'''

class Solution:
    
    def isValid(self, s):
        
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0
    
    def calLR(self, s):
        l, r = 0, 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
        return l, r
    
    def dfs(self, s, index, l, r, res):
        
        if l == 0 and r == 0 and self.isValid(s):
            res.append(s[:])
            return
        
        for i in range(index, len(s)):
            
            if i != index and s[i] == s[i-1]:
                continue
            
            if s[i] == '(':
                news = s[:i] + s[i+1:]
                if l > 0:
                    self.dfs(news, i, l-1, r, res)
            elif s[i] == ')':
                news = s[:i] + s[i+1:]
                if r > 0:
                    self.dfs(news, i, l, r-1, res)
        
        return 0
            
    
    def removeInvalidParentheses(self, s):
        
        res = []
        l, r = self.calLR(s)
        self.dfs(s, 0, l, r, res)
        
        return res


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.removeInvalidParentheses(")("))



























