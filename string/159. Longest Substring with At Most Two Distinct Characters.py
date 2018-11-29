'''
Xiaochi Ma
2018-11-28
'''

class Solution(object):
    
    def lengthOfLongestSubstringTwoDistinct(self, s):
        
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        count = 1
        diff = set()
        diffcount = {}
        j = 0
        for i in range(len(s)):
            while j < len(s) and len(diff) <= 2:
                diff.add(s[j])
                diffcount[s[j]] = diffcount.get(s[j], 0) + 1
                if len(diff) > 2:
                    j += 1
                    break
                count = max(count, j-i+1)
                j += 1
            if s[i] in diff:
                diffcount[s[i]] -= 1
                if diffcount[s[i]] == 0:
                    diff.remove(s[i])
        return count

if __name__ == '__main__':
    
    solution = Solution()
    print(solution.lengthOfLongestSubstringTwoDistinct("ababffzzeee"))  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    