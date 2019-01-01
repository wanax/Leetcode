'''
Xiaochi Ma
2018-12-30
'''

class Solution:
    
    def countRangeSum(self, nums, lower, upper):
        
        pre = [0]
        for num in nums:
            pre.append(pre[-1]+num)
        
        def merge(l, h):
            mid = (l+h)//2
            if mid == l:
                return 0
            count = merge(l, mid) + merge(mid, h)
            i = j = mid
            for k in pre[l:mid]:
                while i < h and pre[i] - k < lower:
                    i += 1
                while j < h and pre[j] - k <= upper:
                    j += 1
                count += (j-i)
            pre[l:h] = sorted(pre[l:h])
            return count
        
        return merge(0, len(pre))
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.countRangeSum([-2,5,-1], -2, 2))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    