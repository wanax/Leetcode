'''
Xiaochi Ma
2018-12-11
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    
    def lowestCommonAncestor(self, root, p, q):
        
        if not root:
            return None
        
        if root.val == p or root.val == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        elif left and not right:
            return left
        elif right and not left:
            return right
        
        return None
    
if __name__ == '__main__':
    
    root = TreeNode(6)
    node1 = TreeNode(2)
    node2 = TreeNode(8)
    node3 = TreeNode(0)
    node4 = TreeNode(4)
    node5 = TreeNode(7)
    node6 = TreeNode(9)
    node7 = TreeNode(3)
    node8 = TreeNode(5)
    
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    node4.left = node7
    node4.right = node8
    
    solution = Solution()
    print(solution.lowestCommonAncestor(root, 2, 8))     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    