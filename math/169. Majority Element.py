'''
Xiaochi Ma
2018-11-30
'''

class Solution(object):
    
    def majorityElement(self, nums):
        
        count = len(nums)/2
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            if dic[num] > count:
                return num
        
        return 0
    
    def __init__(self):
        self.nums = []

        

    def add(self, number):
        self.nums.append(number)
        

    def find(self, value):
        if value == 0 and len(self.nums) > 0:
            return True
        numset = set(self.nums)
        for num in self.nums:
            target = value - num
            if target == 0:
                return True
            if target in numset:
                return True
        return False
    
    def convertToTitle(self, n):
        
        res = []
        while n > 0:
            res.insert(0, chr((n-1)%26+65))
            n = (n-1)//26

        return "".join(res)
    
    def titleToNumber(self, s):
        
        b = 0
        total = 0
        for t in s[::-1]:
            total += (ord(t)-64) * 26**b
            b += 1
        
        return total
    
    def trailingZeroes(self, n):
        
        if n < 5:
            return 0
        if n < 10:
            return 1
        
        return n//5 + self.trailingZeroes(n/5)
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.trailingZeroes(6))  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    