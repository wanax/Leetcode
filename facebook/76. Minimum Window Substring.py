'''
Xiaochi Ma
2018-11-02
'''

class Solution:
    
    def minWindow(self, s, t):
        
        freq = {}
        total = len(t)
        for c in t:
            freq[c] = freq.get(c, 0) + 1
            
        begin, l, r = 0, 0, 0
        minLen = 2**31 - 1
        
        for r in range(len(s)):
            if s[r] in freq:
                if freq[s[r]] > 0:
                    total -= 1
                freq[s[r]] -= 1
            while total == 0:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    begin = l
                
                if s[l] in freq:
                    freq[s[l]] += 1
                    if freq[s[l]] > 0:
                        total += 1
                l += 1
        
        if minLen == 2**31 -1:
            return ""
        else:
            return s[begin:begin+minLen]
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"))   