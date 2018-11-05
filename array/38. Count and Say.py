'''
Xiaochi Ma
2018-10-26
'''

class Solution:
    
    def generate(self, n, nums):
        
        if n == 0:
            return nums
        newNums = ''
        
        count = 1
        tag = nums[0]
        for i in range(1, len(nums)):
            c = nums[i]
            if c != tag:
                newNums += (str(count)+tag)
                tag = c
                count = 1
                
            else:
                count += 1
        newNums += (str(count)+tag)
        return self.generate(n-1, newNums)
        
    
    def countAndSay(self, n):
        
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        else:
            return self.generate(n-2,'11')


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.countAndSay(6))






















