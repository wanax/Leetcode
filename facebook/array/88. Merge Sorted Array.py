'''
Xiaochi Ma
2018-11-05
'''

class Solution(object):
    
    def merge(self, nums1, m, nums2, n):
        
        i, j = 0, 0
        while j < n:
            while nums1[i] < nums2[j] and i < m:
                i += 1
            if i >= m:
                nums1[i] = nums2[j]
            else:
                for x in range(m, i, -1):
                    nums1[x] = nums1[x-1]
                nums1[i] = nums2[j]
            m += 1
            j += 1
        
        return nums1



if __name__ == '__main__':
    
    solution = Solution()
    print(solution.merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3))


















