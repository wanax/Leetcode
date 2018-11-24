'''
Xiaochi Ma
2018-11-21
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    
    def dfs(self, root, res, cur, target):
        
        if not root:
            return
        
        cur.append(root.val)
        
        if sum(cur) == target and not root.left and not root.right:
            res.append(cur[:])
            return
        
        self.dfs(root.left, res, cur[:], target)
        self.dfs(root.right, res, cur[:], target)
        
        return 
    
    def pathSum(self, root, sum):
        
        if not root:
            return []
        res = []
        self.dfs(root, res, [], sum)
        return res
    
    def helper(self, root):
        
        if not root:
            return
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        leftBottom = left
        while leftBottom and leftBottom.right:
            leftBottom = leftBottom.right
        
        if left:
            if right:
                root.right = left
                leftBottom.right = right
            else:
                root.right = left
        root.left = None
        return root
    
    def flatten(self, root):
        
        if not root:
            return
        
        self.helper(root)
    
if __name__ == '__main__':
    
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(5)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(6)
    
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5

    solution = Solution()
    print(solution.flatten(root)) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    