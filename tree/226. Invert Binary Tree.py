'''
Xiaochi Ma
2018-12-09
'''
import sys
from functools import reduce

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    
    def invertTree(self, root):
        
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        
        return root
    
    def dfs(self, root, cur, res):
        
        if not root:
            return
        
        if len(cur) == 0:
            cur += str(root.val)
        else:
            cur += '->'+str(root.val)
            
        if not root.left and not root.right:
            res.append(cur)
            return
            
        self.dfs(root.left, cur, res)
        self.dfs(root.right, cur, res)
    
    def binaryTreePaths(self, root):
        
        if not root:
            return []
        
        res = []
        self.dfs(root, "", res)
        
        return res
    
    def addDigits(self, num):
        
        while len(str(num)) > 1:
            t = 0
            for i in range(len(str(num))):
                t += int(str(num)[i])
            num = t
        
        return num
    
    def threeSumSmaller(self, nums, target):
         
        count = 0
        nums.sort(key=lambda x:x)
        for i in range(len(nums)-2):
            
            l, r = i+1, len(nums)-1
            
            while l < r:
                if l < r and nums[i] + nums[l] + nums[r] < target:
                    count += r-l
                    l += 1
                else:
                    r -= 1

        return count
    
    
    def singleNumber(self, nums):
        
        arr = []
        for num in nums:
            if num in arr:
                arr.remove(num)
            else:
                arr.append(num)
        
        return arr
    
if __name__ == '__main__':
    
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    
    root.left = node1
    root.right = node2
#    node1.left = node3
    node1.right = node4

    solution = Solution()
    print(solution.singleNumber([0,1,2,2])) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    