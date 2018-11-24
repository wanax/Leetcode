'''
Xiaochi Ma
2018-11-10
'''

class Solution:
    
    def shortestPalindrome(self, s):
        
        reverse = s[::-1]
        for i in range(len(s)):
            if s[:len(s)-i] == reverse[i:]:
                return reverse[:i] + s
        
        return ""
    
def getNext(s):
    
    nest = [0] * len(s)
    nest[0] = 0
    for i in range(1, len(s)):
        t = nest[i-1]
        while t > 0 and s[i] != s[t]:
            t = nest[t-1]
        if s[i] == s[t]:
            t += 1
        nest[i] = t
    return nest
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.shortestPalindrome("aacecaaa"))
    
#    print(getNext('aacecaaa#aaacecaa'))