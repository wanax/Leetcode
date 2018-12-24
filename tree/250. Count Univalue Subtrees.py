'''
Xiaochi Ma
2018-12-13
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    
    def __init__(self):
        self.res = 0
        
    def helper(self, root, val):
        
        if not root:
            return True
        
        left = self.helper(root.left, root.val)
        right = self.helper(root.right, root.val)
        
        if not left or not right:
            return False
        
        self.res += 1
        
        return root.val == val
        
    
    def countUnivalSubtrees(self, root):
        
        if not root:
            return 0
        
        self.helper(root, 0)
        
        return self.res
    
if __name__ == '__main__':
    
    root = TreeNode(5)
    node1 = TreeNode(1)
    node2 = TreeNode(5)
    node3 = TreeNode(5)
    node4 = TreeNode(5)
    node5 = TreeNode(5)
    
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5

    solution = Solution()
    print(solution.countUnivalSubtrees(root)) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    