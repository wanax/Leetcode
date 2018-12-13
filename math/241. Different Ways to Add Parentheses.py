'''
Xiaochi Ma
2018-12-12
'''

class Solution(object):
    
    def op(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        elif op == '*':
            return n1 * n2
    
    def diffWaysToCompute(self, input, mem={}):
        
        if input.isdigit():
            return [int(input)]
        if input in mem:
            return mem[input]
        
        ops = {'+', '-', '*'}
        
        res = []
        for i in range(len(input)):
            if input[i] in ops:
                r1 = self.diffWaysToCompute(input[:i], mem)
                r2 = self.diffWaysToCompute(input[i+1:], mem)
                for n in range(len(r1)):
                    for m in range(len(r2)):
                        res.append(self.op(r1[n], r2[m], input[i]))
        mem[input] = res
        return res
    
    def helper(self, num, target, path, total, pre, res):

        if len(num) == 0:
            if total == target:
                res.append(path)
            return
        
        for i in range(len(num)):
            cur = int(num[:i+1])
            if len(path) == 0:
                self.helper(num[i+1:], target, path+num[:i+1], cur, cur, res)
            else:
                self.helper(num[i+1:], target, path+'+'+num[:i+1], total+cur, cur, res)
                self.helper(num[i+1:], target, path+'-'+num[:i+1], total-cur, -cur, res)
                v = total - pre + pre*cur
                self.helper(num[i+1:], target, path+'*'+num[:i+1], v, pre*cur, res)
                
    def addOperators(self, num, target):
        
        res = []
        self.helper(num, target, "", 0, 0, res)
        
        return res
    
    def helper2(self, nums, idx, target, path, total, res):
        
        if idx == len(nums):
            if total == target:
                res.append(path)
            return
        
        self.helper2(nums, idx+1, target, path+"+"+str(nums[idx]), total+nums[idx], res)
        self.helper2(nums, idx+1, target, path+"-"+str(nums[idx]), total-nums[idx], res)
    
    def findTargetSumWays(self, nums, S):
        
        res = []
        self.helper2(nums, 0, S, "", 0, res)
        
        return len(res)
    
    def isOneEditDistance(self, s, t):
        
        if len(s) == 0 and len(t) == 0:
            return False
        
        if s == t:
            return False
        
        if len(s) == 0 or len(t) == 0:
            if len(t) == 1 or len(s) == 1:
                return True
        
        for i in range(len(s)):
            for j in range(len(t)):
                if s[:i]+s[i+1:] == t[:j]+t[j+1:] or\
                s[:i]+s[i+1:] == t or \
                s == t[:j]+t[j+1:]:
                    return True
        
        return False
    
if __name__ == '__main__':
    
    solution = Solution()
#    print(solution.diffWaysToCompute("2*3-4*5"))
#    print(solution.addOperators("232", 8))
    print(solution.isOneEditDistance("ab","ba"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    