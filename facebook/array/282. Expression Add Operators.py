'''
Xiaochi Ma
2018-11-05
'''

class Solution(object):
    
    def __init__(self):
        self.nums = ""
        self.target = 0
    
    def helper(self, index, op, total, pre, res):
        
        if index > len(self.nums) - 1:
            if total == self.target:
                res.append(op[:])
            return
        
        curr = 0
        for i in range(index, len(self.nums)):
            
            curr = curr*10 + self.nums[i]
            if index == 0:
                self.helper(i+1, op+str(curr), curr, curr, res)
            else:
                self.helper(i+1, op+'+'+str(curr), total+curr, curr, res)
                self.helper(i+1, op+'-'+str(curr), total-curr, -curr, res)
                value = total - pre + pre*curr
                self.helper(i+1, op+'*'+str(curr), value, pre*curr, res)
                
            if self.nums[index] == 0:
                break
    
    def addOperators(self, num, target):
        
        if len(num) == 0:
            return []
        
        self.nums = list(map(int, num))
        self.target = target
        res = []
        self.helper(0, "", 0, 0, res)
        return res


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.addOperators("00", 0))
    






















