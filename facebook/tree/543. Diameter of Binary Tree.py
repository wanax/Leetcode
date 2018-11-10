'''
Xiaochi Ma
2018-11-09
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def helper(self, root):
        
        if root is None:
            return 0
        
        l = self.helper(root.left)
        r = self.helper(root.right)
        
        now = l + r + 1
        if now > self.maxs:
            self.maxs = now
        return max(l, r) + 1
    
    def diameterOfBinaryTree(self, root):
        
        if root is None:
            return 0
        
        self.maxs = 0
        self.helper(root)
        return self.maxs-1
    
if __name__ == '__main__':
    
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    
    
    solution = Solution()
    print(solution.diameterOfBinaryTree(root))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    