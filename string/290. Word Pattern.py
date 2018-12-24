'''
Xiaochi Ma
2018-12-22
'''
import itertools
class Solution(object):
    
    def wordPattern(self, pattern, str):
        
        dic = {}
        for i in range(len(pattern)):
            c = pattern[i]
            pos = dic.get(c, [])
            pos.append(i)
            dic[c] = pos
        
        dic2 = {}
        words = str.split(" ")
        for i in range(len(words)):
            word = words[i]
            pos = dic2.get(word, [])
            pos.append(i)
            dic2[word] = pos
            
        if len(dic) != len(dic2):
            return False
        
        arr1 = list(dic.values())
        arr1.sort(key=lambda x:x[0])
        arr2 = list(dic2.values())
        arr2.sort(key=lambda x:x[0])
        
        return True if arr1 == arr2 else False
    
    def dfs(self, s, pat, dic):
        
        if len(pat) == 0:
            if len(s) == 0:
                return True
            else:
                return False
        
        for i in range(1, len(s)+1):
            c = pat[0]
            key = s[:i]
            if c in dic:
                if dic[c] == key:
                    res = self.dfs(s[i:], pat[1:], dic)
                    if res:
                        return True
            else:
                if key not in dic.values():
                    dic[c] = key
                    res = self.dfs(s[i:], pat[1:], dic)
                    dic.pop(c, None)
                    if res:
                        return True
        return False
                    
    
    def wordPatternMatch(self, pattern, str):
        
        if len(pattern) == 0 and len(str) != 0:
            return False
        
        dic = {}
        res = self.dfs(str, pattern, dic)
        
        return res
    
    def divid(self, s):
        
        if len(s) <= 1:
            return [0]
        
        res = set()
        for i in range(len(s)-1):
            if s[i] == s[i+1] == '+':
                ls = self.divid(s[:i])
                rs =self.divid(s[i+2:])
                tmp = set([r[0]+r[1]+1 for r in itertools.product(ls, rs)])
                res |= tmp
        return res
    
    def win(self, s, dic):
        
        if s in dic:
            return dic[s]
        if '++' not in s:
            return False
        
        for i in range(len(s)-1):
            if s[i:i+2] == '++':
                tmp = s[:i]+'--'+s[i+2:]
                if not self.win(tmp, dic):
                    dic[s] = True
                    return True
        dic[s] = False
        return False
    
    def canWin(self, s):

        dic = {}
        return self.win(s, dic)
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.canWin("+++++++++"))
#    t = [r[0]+r[1] for r in itertools.product([1,2,3], [4,5,6])]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    