'''
Xiaochi Ma
2018-12-15
'''
import sys
class Solution(object):
    
    def divid(self, arr, rang):
        
        if len(arr) == 0:
            return True
        
        if len(arr) == 1:
            if arr[0] >= rang[0] and arr[0] <= rang[-1]:
                return True
            else:
                return False
        
        idx = len(arr)
        f = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > f and idx == len(arr):
                idx = i
            if arr[0] < rang[0] or arr[0] > rang[-1]:
                return False

        left = self.divid(arr[1:idx], [rang[0], f-1])
        right = self.divid(arr[idx:], [f+1, rang[-1]])
        
        return left and right
    
    def verifyPreorder(self, preorder):
        
        stack = []
        low = -sys.maxsize
        for item in preorder:
            if item < low:
                return False
            while stack and stack[-1] < item:
                low = stack.pop()
            stack.append(item)
        return True
#        return self.divid(preorder, [-sys.maxsize, sys.maxsize])
    
if __name__ == '__main__':
    

    solution = Solution()
    print(solution.verifyPreorder([3, 1, 2])) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    