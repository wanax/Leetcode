'''
Xiaochi Ma
2018-11-01

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
'''

class Solution:
    
    def recursive(self, s, l, r, errors):
        
        if len(s) == 1 or len(s) == 2:
            return True
        
        if l > r:
            return False
        if r - l <= 1:
            if r == l:
                return True
            else:
                if s[r] == s[l]:
                    return True
                else:
                    return False
        
        tag = False
        while r - l > 1:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if errors > 0:
                    errors -= 1
                    return self.recursive(s, l+1, r, errors) or self.recursive(s, l, r-1, errors)
                else:
                    return False
        if r - l <= 1:
            return True
        return tag
    
    def validPalindrome(self, s):
        
        return self.recursive(s, 0, len(s)-1, 1)
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.validPalindrome("yd"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    