'''
Xiaochi Ma
2018-11-20
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    
    def maxDepth(self, root):
        
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1
    
    def levelRecursion(self, root, levels, level):
        
        if level >= len(levels):
            return
        
        if not root:
            return
        
        arr = levels[level]
        arr.append(root.val)
        self.levelRecursion(root.left, levels, level+1)
        self.levelRecursion(root.right, levels, level+1)
        
    
    def levelOrder(self, root):
        
        n = self.maxDepth(root)
        levels = [[] for i in range(n)]
        
        self.levelRecursion(root, levels, 0)
        
        return levels
    
    
    def buildTree2(self, preorder, inorder):
        
        if len(inorder) == 0 or len(preorder) == 0:
            return
        
        val = preorder.pop(0)
        i = inorder.index(val)
        
        root = TreeNode(val)
        
        root.left = self.buildTree2(preorder, inorder[:i])
        root.right = self.buildTree2(preorder, inorder[i+1:])
        
        return root
    
    def buildTree(self, inorder, postorder):
        
        if len(inorder) == 0 or len(postorder) == 0:
            return
        
        val = postorder.pop()
        i = inorder.index(val)
        
        root = TreeNode(val)
        root.right = self.buildTree(inorder[i+1:], postorder)
        root.left = self.buildTree(inorder[:i], postorder)
        
        return root
    
    def toBSTRecursion(self, nums, l, r):
        
        if l > r:
            return None
        
        mid = (l + r)//2
        val = nums[mid]
        root = TreeNode(val)
        
        root.left = self.toBSTRecursion(nums, l, mid-1)
        root.right = self.toBSTRecursion(nums, mid+1, r)
        
        return root
    
    def sortedArrayToBST(self, nums):
        
        if len(nums) == 0:
            return None
        
        return self.toBSTRecursion(nums, 0, len(nums)-1)
    def diffDepth(self, root):
        
        if not root:
            return 0
        left = self.diffDepth(root.left)
        right = self.diffDepth(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    
    def isBalanced(self, root):
        
        if not root:
            return True
        
        return True if self.diffDepth(root) != -1 else False
    
    
if __name__ == '__main__':
    
    root = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)
    
    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    
    solution = Solution()
    print(solution.isBalanced(root))     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    