'''
Xiaochi Ma
2018-12-15
'''

class Solution(object):
    
    def helper(self, n, idx, cur, res):
        
        if n==1:
            if len(cur) > 1:
                res.append(cur[:])
            return
        
        while idx*idx <= n:
            if n%idx==0:
                res.append(cur+[idx, n//idx])
                cur.append(idx)
                self.helper(n//idx, idx, cur, res)
                cur.pop()
            idx += 1
        
    
    def getFactors(self, n):
        
        if n == 0 or n == 1:
            return []
        
        res = []
        self.helper(n, 2, [], res)
        
        return res
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.getFactors(32))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    