'''
Xiaochi Ma
2018-11-08
'''

import heapq

class Solution:
    
    def findKthLargest(self, nums, k):
        
        heap = [-1] * k
        for n in nums:
            if n > heap[0]:
                if len(heap) == k:
                    heapq.heappop(heap)
                    heapq.heappush(heap, n)
                else:
                    heapq.heappush(heap, n)
        
        return heap[0]
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    