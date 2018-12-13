'''
Xiaochi Ma
2018-12-09
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def rightt(self, root):
        
        if not root:
            return 0
        count = 0
        while root:
            root = root.right
            count += 1
        return count
    def leftt(self, root):
        if not root:
            return 0
        count = 0
        while root:
            root = root.left
            count += 1
        return count
    
    def countNodes(self, root):
        
        if not root:
            return 0
        left = self.leftt(root.left)
        right = self.rightt(root.right)
        if left == right:
            total = 1
            for i in range(1, left+1):
                total += 2**i
            return total
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
if __name__ == '__main__':
    
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    node5 = TreeNode(6)
    
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5

    solution = Solution()
    print(solution.countNodes(root)) 
    
    
