'''
Xiaochi Ma
2018-11-04
'''
import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def back(self, root, res, cur):
        
        if root is None:
            return cur
        if root.val > 0:
            cur.append(root.val)
            curLeft = self.back(root.left, res, [])
            curRight = self.back(root.right, res, [])
            if curLeft is not None and sum(curLeft) > 0:
                cur += curLeft
            if curRight is not None and sum(curRight) > 0:
                cur += curRight
            return cur
        else:
            res.append(self.back(root.left, res, []))
            res.append(self.back(root.right, res, []))
    
    def maxPathSum2(self, root):
        
        if root is None:
            return 0
        res = []
        res.append(self.back(root, res, []))
        
        maxV = 0
        for items in res:
            if items is None:
                continue
            if sum(items) > maxV:
                maxV = sum(items)
        
        return maxV
    
    res = -sys.maxsize
    
    def helper(self, root):
        
        if root is None:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        temp = root.val + left + right
        sumV = root.val + max(left, right, 0)
        self.res = max(sumV, temp, self.res)
        
        return sumV
    
    def maxPathSum(self, root):
        
        if root is None:
            return 0
        
        self.helper(root)
        return self.res



if __name__ == '__main__':
    
#    root = TreeNode(-10)
#    node1 = TreeNode(9)
#    node2 = TreeNode(20)
#    node3 = TreeNode(15)
#    node4 = TreeNode(7)
#    
#    root.left = node1
#    root.right = node2
#    node2.left = node3
#    node2.right = node4
    
    root = TreeNode(2)
    node1 = TreeNode(-1)
    root.left = node1
    
    solution = Solution()
    print(solution.maxPathSum(root))     

























