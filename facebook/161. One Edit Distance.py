'''
Xiaochi Ma
2018-11-12
'''

class Solution:
    
    def isOneEditDistance(self, s, t):
        
        i = 0
        while i < len(s) and i < len(t):
            if s[i] == t[i]:
                i += 1
                continue
            else:
                return s[i+1:] == t[i:] or s[i:] == t[i+1:] or s[i+1:] == t[i+1:]
        
        return abs(len(s) - len(t)) == 1
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.isOneEditDistance("1203", "1213"))



















