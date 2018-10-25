'''
Xiaochi Ma
2018-10-21
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def infindVal(self, root, res):
        
        if root.left:
            self.infindVal(root.left, res)
            
        res.append(root.val)
        
        if root.right:
            self.infindVal(root.right, res)
        
    
    def inorderTraversal(self, root):
        
        res = []
        if root:
            self.infindVal(root, res)
        
        return res
    
    def preFindVal(self, root, res):
        
        res.append(root.val)
        if root.left:
            self.preFindVal(root.left, res)
        if root.right:
            self.preFindVal(root.right, res)
    
    def preTraversal(self, root):
        
        res = []
        if root:
            self.preFindVal(root, res)
        return res
    
    def postFindVal(self, root, res):
        
        if root.left:
            self.postFindVal(root.left, res)
        if root.right:
            self.postFindVal(root.right, res)
        res.append(root.val)
    
    def postTraversal(self, root):
        
        res = []
        if root:
            self.postFindVal(root, res)
        
        return res
        
        
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
    print(solution.postTraversal(root))        
        
        
        
        
        
        
        