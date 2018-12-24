'''
Xiaochi Ma
2018-12-13
'''

class Solution(object):
    
    def helper(self, cur, res, l, r):
        
        if l > r:
            res.append(cur[:])
            return
        if l == r:
            cur[l] = '0'
            res.append(cur[:])
            cur[l] = '1'
            res.append(cur[:])
            cur[l] = '8'
            res.append(cur[:])
            return
        
        if l != 0:
            cur[l], cur[r] = '0', '0'
            self.helper(cur, res, l+1, r-1)
            
        cur[l], cur[r] = '1', '1'
        self.helper(cur, res, l+1, r-1)
        
        cur[l], cur[r] = '6', '9'
        self.helper(cur, res, l+1, r-1)
        
        cur[l], cur[r] = '8', '8'
        self.helper(cur, res, l+1, r-1)
        
        cur[l], cur[r] = '9', '6'
        self.helper(cur, res, l+1, r-1)
    
    def findStrobogrammatic(self, n):
        
        res = []
        cur = ['' for i in range(n)]
        self.helper(cur, res, 0, n-1)
        
        return ["".join(item) for item in res]
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.findStrobogrammatic(3))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    