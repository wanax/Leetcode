'''
Xiaochi Ma
2018-12-17
'''
from functools import reduce
import collections
class Solution(object):
    
    def canPermutePalindrome(self, s):
        
        dic = {}
        
        for c in s:
            v = dic.get(c, 0)
            dic[c] = v ^ 1
        
        total=reduce(lambda total, val: total+val, dic.values(), 0)
        
        return True if total==0 or total==1 else False
    
    def bfs(self, dic, cur, res, l, r):
        
        if l > r:
            res.append(cur[:])
            return
        if l == r:
            c = ''
            for key, v in dic.items():
                if v == 1:
                    c = key
            cur[l] = c
            res.append(cur[:])
            
        for key, v in dic.items():
            if v > 1:
                cur[l], cur[r] = key, key
                dic[key] -= 2
                self.bfs(dic, cur, res, l+1, r-1)
                cur[l], cur[r] = '',''
                dic[key] += 2
                    
    
    def generatePalindromes(self, s):
        
        dic = {}
        
        for c in s:
            dic[c] = dic.get(c, 0) + 1
            
        cur = ['' for i in range(len(s))]
        res = []
        self.bfs(dic, cur, res, 0, len(s)-1)
        
        return list(map(lambda x : "".join(x), res))
    
    
    def generatePalindromes2(self, s):
        # d = collections.Counter(s)
        # m = tuple(k for k, v in d.iteritems() if v % 2)
        # p = ''.join(k*(v/2) for k, v in d.iteritems())
        # return [''.join(i + m + i[::-1]) for i in set(itertools.permutations(p))] if len(m) < 2 else []
        
        def dfs(depth, base):
            if depth == len(base):
                res.append(base+mid+base[::-1])
                return
            for i in range(depth, len(base)):
                if i > depth and (base[i] == base[i-1] or base[i] == base[depth]):
                    continue
                # swap i and depth in base
                # abcdefg
                #   d  i 
                perm = base if i == depth else base[:depth] + base[i] + base[depth+1:i] + base[depth] + base[i+1:]
                dfs(depth+1, perm)
        d = collections.Counter(s)
        mids = []
        base = ''
        res = []
        for k, v in d.iteritems():
            if v % 2:
                mids += k,
            base += (v/2) * k
        if len(mids) > 1:
            return []
        mid = '' if mids == [] else mids[0]
        dfs(0, base)
        return res
    
    def missingNumber(self, nums):
        
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.missingNumber([0]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    