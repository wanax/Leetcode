'''
Xiaochi Ma
2018-11-28
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def total(self, root):
        
        if not root:
            return 0
        left = self.total(root.left)
        right = self.total(root.right)
        return 1 + left + right
    
    def pre(self, root, res, k):
        if not root or len(res) == k:
            return
        if root.left:
            self.pre(root.left, res, k)
        if len(res) == k:
            return
        res.append(root.val)
        if root.right:
            self.pre(root.right, res, k)
    
    def kthSmallest(self, root, k):
        
        res = []
        self.pre(root, res, k)
        return res[-1]
    
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
    print(solution.kthSmallest(root, 3)) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    