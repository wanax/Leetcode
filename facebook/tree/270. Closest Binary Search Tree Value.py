'''
Xiaochi Ma
2018-11-12
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    
    def __init__(self):
        self.res = 2**61 - 1
    
    def helper(self, root, target):
        
        if root is None:
            return
        
        if abs(root.val - target) < abs(self.res - target):
            self.res = root.val
        
        self.helper(root.left, target)
        self.helper(root.right, target)
        
        return
    
    def closestValue(self, root, target):
        
        if root is None:
            return 0
        
        self.helper(root, target)
        
        return self.res


if __name__ == '__main__':
    
    root = TreeNode(1)
    node1 = TreeNode(2)
#    node2 = TreeNode(5)
#    node3 = TreeNode(1)
#    node4 = TreeNode(3)
#    
    root.right = node1
#    root.right = node2
#    node1.left = node3
#    node1.right = node4
    
    
    solution = Solution()
    print(solution.closestValue(root, 3.428571))























