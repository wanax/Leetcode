'''
Xiaochi Ma
2018-12-09
'''

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
    print(solution.invertTree(root)) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    