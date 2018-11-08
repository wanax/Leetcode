'''
Xiaochi Ma
2018-11-06
'''
import random
class Solution(object):

    def __init__(self, nums):
        self.dic = {}
        for i in range(len(nums)):
            vs = self.dic.get(nums[i], [])
            vs.append(i)
            self.dic[nums[i]] = vs
        

    def pick(self, target):
        vs = self.dic[target]
        return vs[random.randint(0,len(vs)-1)]
    
    
if __name__ == '__main__':
    
    obj = Solution([1,2,3,3,3])
    print(obj.pick(1))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    