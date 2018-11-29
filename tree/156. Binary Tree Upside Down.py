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
    
    def upsideDownBinaryTree(self, root):
        
        if not root:
            return None
        if not root.left and not root.right:
            return root
        
        leftree = self.upsideDownBinaryTree(root.left)
        
        root.left.left = root.right
        root.left.right = root
        root.left, root.right = None, None
        
        return leftree
    
    def getIntersectionNode(self, headA, headB):
        
        if not headA or not headB:
            return None
        
        pa = headA
        pb = headB
        while pa != pb:
            pa = headA if pa is None else pa.next
            pb = headB if pb is None else pb.next
        
        return pa
        
    
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
    print(solution.upsideDownBinaryTree(root)) 