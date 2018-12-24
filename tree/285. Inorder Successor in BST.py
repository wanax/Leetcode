'''
Xiaochi Ma
2018-12-21
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    
    def inorderSuccessor(self, root, p):

        succ = None
        while root:
            if root.val > p:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ.val if succ else None

    
if __name__ == '__main__':
    
    root = TreeNode(5)
    node1 = TreeNode(3)
    node2 = TreeNode(6)
    node3 = TreeNode(2)
    node4 = TreeNode(4)
    node5 = TreeNode(1)
    
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node3.left = node5

    solution = Solution()
    print(solution.inorderSuccessor(root, 4)) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    