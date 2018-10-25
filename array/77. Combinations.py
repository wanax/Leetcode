'''
Xiaochi Ma
2018-10-23
'''

class Solution:
    
    def backtracking(self, n, k, res, curArr, index):
        if len(curArr) == k:
            res.append(curArr[:])
            return
        for i in range(index, n+1):
            curArr.append(i)   
            self.backtracking(n, k, res, curArr, i+1)
            curArr.pop()
        
    
    def combine(self, n, k):
        
        if n == 0 or k == 0:
            return []
        
        res = []
        self.backtracking(n, k, res, [], 1)
        return res



if __name__ == '__main__':
    
    solution = Solution()
    print(solution.combine(4,3)) 
    























