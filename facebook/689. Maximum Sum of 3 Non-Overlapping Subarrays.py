'''
Xiaochi Ma
2018-11-09
'''

class Solution:
    
    def maxSumOfThreeSubarrays(self, nums, k):
        
        sums = []
        
        sum_ = 0
        for i, num in enumerate(nums):
            sum_ += num
            if i >= k:
                sum_ -= nums[i-k]
            if i >= k-1:
                sums.append(sum_)
            
        max_left = [0] * len(sums)
        best = 0
        for i in range(len(sums)):
            if sums[i] > sums[best]:
                best = i
            max_left[i] = best
        
        max_right = [0] * len(sums)
        best = len(sums) - 1
        for i in range(len(sums)-1, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            max_right[i] = best        

        res = []
        for n in range(k, len(sums)-k):
            left = max_left[n-k]
            right = max_right[n+k]
            if len(res) == 0 or (sums[n] + sums[left] + sums[right] > sums[res[0]] + sums[res[1]] + sums[res[2]]):
                res = [left, n, right]
        
        return res
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.maxSumOfThreeSubarrays([7,13,20,19,19,2,10,1,1,19], 3))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    