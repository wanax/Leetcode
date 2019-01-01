'''
Xiaochi Ma
2018-12-29
'''
from collections import OrderedDict

class Solution:
    
    def removeDuplicateLetters2(self, s):
        
        if not s: return ''
        
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        
        last = OrderedDict(sorted(last.items(), key=lambda x:x[1]))
        start, end = 0, list(last.items())[0][1]
        ans = []
        for i in range(len(last)):
            min_c = 'z'
            for k in range(start, end+1):
                if min_c > s[k] and s[k] in last:
                    min_c = s[k]
                    start = k+1
            ans.append(min_c)
            last.pop(min_c)
            if not last:
                break
            end = list(last.items())[0][1]
        
        return "".join(ans)
    
    def removeDuplicateLetters(self, s):
        
        cnt = [0]*26
        for c in s:
            cnt[ord(c)-97] += 1
        
        ans = []
        for c in s:
            cnt[ord(c)-97] -= 1
            if c in ans:
                continue
            while ans and ans[-1] > c and cnt[ord(ans[-1])-97] > 0:
                ans.pop()
            ans.append(c)
        
        return "".join(ans)
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.removeDuplicateLetters("dcbacdcd"))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    