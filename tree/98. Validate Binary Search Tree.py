'''
Xiaochi Ma
2018-11-19
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
import sys       
class Solution:
    
    def helper(self, root, low, up):
        
        if root is None:
            return True
        
        if root.val <= low or root.val >= up:
            return False
        
        left = self.helper(root.left, low, root.val)
        right = self.helper(root.right, root.val, up)
        
        return left and right
    
    def isValidBST(self, root):
        
        return self.helper(root, -sys.maxsize, sys.maxsize)
    
    
    def isSameTree(self, p, q):
        
        if not p:
            return True if p == q else False
        elif not q:
            return True if p == q else False
        
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        return left and right
    
    def isMirror(self, p, q):
        
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        
        return q.val == p.val and self.isMirror(p.left, q. right) and self.isMirror(p.right, q.left)
    
    def isSymmetric(self, root):
        
        return self.isMirror(root, root)
    
    def recoverTree(self, root):
        
        
        
        return 0
        
        
if __name__ == '__main__':
    
    root = TreeNode(5)
    node1 = TreeNode(1)
    node2 = TreeNode(4)
    node3 = TreeNode(3)
    node4 = TreeNode(6)
    
    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    
    solution = Solution()
    print(solution.isSymmetric(root))            
        
        
        
        
        
        
        
        
        
        
        
        
        
        