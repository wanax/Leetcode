'''
Xiaochi Ma
2018-10-26
'''

class Solution:
    def firstMissingPositive(self, nums):
                                       
           n = len(nums)
           
           i = 0
           while i < n:
               
               num = nums[i]
               if num == i + 1:
                   i += 1
                   continue
               
               if nums[i] > 0 and nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[nums[i]-1]:
                   temp = nums[nums[i] - 1]
                   nums[nums[i] - 1] = nums[i]
                   nums[i] = temp
               else:
                   i += 1
                   
                   
           for i in range(n):
               if nums[i] != i + 1:
                   return i+1
           
           return n+1

if __name__ == '__main__':
    
    solution = Solution()
    print(solution.firstMissingPositive([3,4,-1,1]))

















