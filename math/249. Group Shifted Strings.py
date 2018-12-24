'''
Xiaochi Ma
2018-12-13
'''

class Solution(object):
    
    def getPatten(self, s):
        
        if len(s) == 1:
            return "-1"
        p = ""
        for i in range(1, len(s)):
            p += str((26 + ord(s[i]) - ord(s[i-1]))%26)
            
        return p
    
    def groupStrings(self, strings):
        
        groups = {}
        
        for string in strings:
            p = self.getPatten(string)
            arr = groups.get(p, [])
            arr.append(string)
            groups[p] = arr
        
        return groups.values()

if __name__ == '__main__':
    
    solution = Solution()
    print(solution.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    