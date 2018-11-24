'''
Xiaochi Ma
2018-11-12
'''

class Solution(object):
    
    def lengthOfLongestSubstringKDistinct(self, s, k):
        
        dic = {}
        l, r = 0, 0
        total = 0
        max_len = 0
        while l < len(s) and r < len(s):
            dic[s[r]] = dic.get(s[r], 0) + 1
            if dic[s[r]] == 1:
                total += 1
            if total <= k:
                max_len = max(max_len, r-l+1)                
            while total > k:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    total -= 1
                l += 1
            r += 1
        
        return max_len
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.lengthOfLongestSubstringKDistinct("eceba", 2))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    