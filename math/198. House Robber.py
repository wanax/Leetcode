'''
Xiaochi Ma
2018-12-05
'''

class Solution(object):
    
    def back(self, nums, index):
        
        if index >= len(nums):
            return 0
        
        return max(nums[index]+self.back(nums, index+2), self.back(nums, index+1))
    
    def rob2(self, nums):
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        return dp[len(nums)-1]
    
    def rangeBitwiseAnd(self, m, n):
        
        i = 0
        while m != n:
            i += 1
            m >>= 1
            n >>= 1
        
        
        return m << i
    
    def isHappy(self, n):
        
        res = 0
        count = 1
        while count < 10:
            res = 0
            while n>0:
                res += (n%10)**2
                n = n//10
            if res == 1:
                return True
            count += 1
            n = res
        
        return False
    
    def rob(self, nums):
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1 or len(nums) == 2 or len(nums) == 3:
            return max(nums)
        
        ydp = [0 for i in range(len(nums)+1)]
        ydp[1] = nums[0]
        ndp = [0 for i in range(len(nums)+1)]
        ndp[1] = 0
        
        for i in range(2, len(nums)):
            ydp[i] = max(ydp[i-1], ydp[i-2]+nums[i-1])
        ydp[len(nums)] = ydp[len(nums)-1]
        
        for i in range(2, len(nums)+1):
            ndp[i] = max(ndp[i-1], ndp[i-2]+nums[i-1])
        
        return max(ndp[len(nums)], ydp[len(nums)])
    
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        
        dic = {}
        mm = min(nums)
        size = t + 1
        for i in range(len(nums)):
            n = (nums[i] - mm)//size
            if n in dic:
                return True
            if n-1 in dic and abs(dic[n-1]-nums[i]) <= t:
                return True
            if n+1 in dic and abs(dic[n+1]-nums[i]) <= t:
                return True
            dic[n] = nums[i]
            if i >= k:
                dic.pop(nums[i-k])
            
        return False
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    