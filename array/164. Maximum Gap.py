'''
Xiaochi Ma
2018-11-29
'''

class Solution(object):
    
    def maximumGap(self, nums):
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 0
        
        if len(nums) == 2:
            return abs(nums[1] - nums[0])
        
        m = max(nums)
        n = min(nums)
        bucketSize = max(1, (m - n) // (len(nums) - 1))
        
        dic = {}
        
        for num in nums:
            idx = (num - n) // bucketSize
            arr = dic.get(idx, [])
            arr.append(num)
            dic[idx] = arr
        
        preMax = n
        gap = 0
        for key, item in dic.items():
            if len(item) == 0:
                continue
            gap = max(gap, min(item) - preMax)
            preMax = max(item)
        
        return gap
    
    def compareVersion(self, version1, version2):
        
        vs1 = list(map(lambda x:int(x), version1.split('.')))
        vs2 = list(map(lambda x:int(x), version2.split('.')))
        
        i, j = 0, 0
        while i < len(vs1) and j < len(vs2):
            if int(vs1[i]) - int(vs2[j]) < 0:
                return -1
            elif int(vs1[i]) - int(vs2[j]) > 0:
                return 1
            i += 1
            j += 1
            
        if i == len(vs1) and j == len(vs2):
            return 0
        
        if i == len(vs1) and sum(vs2[j:]) != 0:
            return -1
        if j == len(vs2) and sum(vs1[i:]) != 0:
            return 1
        
        return 0
    
    def fractionToDecimal(self, numerator, denominator):
        
        hashmap = {}
        if numerator * denominator < 0:
            numerator, denominator = abs(numerator), abs(denominator)
        
        res = ""
        numerator %= denominator
        if numerator != 0:
            res += '.'
        
        i = len(res)
        while numerator != 0:
            numerator *= 10
            divi = numerator / denominator
            if numerator in hashmap:
                ind = (hashmap[numerator])
                res = res[:ind] + '(' + res[ind:] + ')'
                break
            else:
                hashmap[numerator] = i
                res += str(divi)
                i += 1
            
            numerator %= denominator
        
        return res
    
    def twoSum(self, numbers, target):
        
        dic = set(numbers)
        res = []
        for i in range(len(numbers)):
            other = target - numbers[i]
            if other in dic:
                res.append(min(i+1, numbers[i+1:].index(other)+i+2))
                res.append(max(i+1, numbers[i+1:].index(other)+i+2))
                break
        
        return res
    
    def convertToTitle(self, n):
        
        res = []
        while n > 0:
            res.insert(0, chr((n-1)%26+65))
            n = (n-1)//26

        return "".join(res)
    
if __name__ == '__main__':
    
    solution = Solution()
#    print(solution.maximumGap([1,1,1,1]))  
#    print(solution.compareVersion("1.0", '1'))  
#    print(solution.twoSum([2,7,11,15], 9)) 
    print(solution.convertToTitle(701)) 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    