#######################

# Machine Learning Test 2018/10/04
# Miles Ma
#
########################
import random

class Solution(object):
    
    def quickSort(self, arr):
    
        if (len(arr) <= 1):
            return arr
        pivot = arr[0]
        less = []
        bigger = []
        for i in range(1, len(arr)):
            item = arr[i]
            if (item >= pivot):
                bigger.append(item)
            else:
                less.append(item)
        mergedList = self.quickSort(less)+ [pivot] + self.quickSort(bigger)
        return mergedList
    
    def findMedianSortedArrays(self, nums1, nums2):
        
        temps = nums1 + nums2
        nums = self.quickSort(temps)
        median = 0.0
        if (len(nums) % 2 == 0):
            median = float((nums[int(len(nums)/2)] + nums[int(len(nums)/2) - 1])/2)
        else:
            median = float(nums[int((len(nums)+1)/2) - 1])
        return median

if __name__ == '__main__':
    
    nums1 = random.sample(range(1000), 10)
    nums2 = random.sample(range(1000), 11)
    
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))
    

#    
#    nums = quickSort(nums1 + nums2)
#    median = 0
#
#    if (len(nums) % 2 == 0):
#        median = (nums[int(len(nums)/2)] + nums[int(len(nums)/2) + 1])/2
#    else:
#        median = nums[int((len(nums)+1)/2)]
#    print(median)
































