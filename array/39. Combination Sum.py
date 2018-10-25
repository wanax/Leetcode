'''
Xiaochi Ma
2018-10-24
'''

class Solution:
    
    def backtracking(self, target, candidates, curArr, res, index):
        if sum(curArr) == target:
            res.append(curArr[:])
            return
        if sum(curArr) > target:
            return
        for i in range(index, len(candidates)):
            curArr.append(candidates[i])
            self.backtracking(target, candidates, curArr, res, i)
            curArr.pop()
    
    def combinationSum(self, candidates, target):
        
        if len(candidates) == 0 or target == 0:
            return []
        
        res = []
        self.backtracking(target, candidates, [], res, 0)
        
        return res
    
    def backtracking2(self, target, candidates, curArr, res, index, used):
        if sum(curArr) == target:
            res.append(curArr[:])
            return
        if sum(curArr) > target:
            return
        for i in range(index, len(candidates)):
            if (i > 0 and candidates[i] == candidates[i-1] and not used[i-1]):
                continue
            used[i] = 1
            curArr.append(candidates[i])
            self.backtracking2(target, candidates, curArr, res, i+1, used)
            used[i] = False
            curArr.pop()
    
    def combinationSum2(self, candidates, target):

        if len(candidates) == 0 or target == 0:
            return []
        
        res = []
        used = [0 for i in range(len(candidates))]
        candidates.sort()
        self.backtracking2(target, candidates, [], res, 0, used)
        
        return res
    
    def backtracking3(self, k, n, res, curArr, index):
        
        if len(curArr) == k and sum(curArr) == n:
            res.append(curArr[:])
        if len(curArr) == k or sum(curArr) > n:
            return
        
        for i in range(index, 10):
            curArr.append(i)
            self.backtracking3(k, n, res, curArr, i+1)
            curArr.pop()
        
    def combinationSum3(self, k, n):
        
        if k == 0 or n == 0:
            return []
        
        res = []
        self.backtracking3(k, n, res, [], 1)
        
        return res

if __name__ == '__main__':
    
    solution = Solution()
    print(solution.combinationSum3(3, 9))



















