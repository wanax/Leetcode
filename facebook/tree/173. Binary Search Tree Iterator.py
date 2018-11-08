'''
Xiaochi Ma
2018-11-05
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    
    def inOrder(self, root):
        
        if root.left:
            self.inOrder(root.left)
        self.res.append(root.val)
        if root.right:
            self.inOrder(root.right)
    
    def __init__(self, root):
        self.res = []
        if root:
            self.inOrder(root)

    def hasNext(self):
        
        return True if len(self.res) > 0 else False
        

    def next(self):
        return self.res.pop(0)


if __name__ == '__main__':
    
    root = TreeNode(3)
    node1 = TreeNode(2)
    node2 = TreeNode(5)
    node3 = TreeNode(1)
    node4 = TreeNode(4)
    node5 = TreeNode(7)
    
    root.left = node1
    root.right = node2
    node1.left = node3
    node2.left = node4
    node2.right = node5

    
    i, v = BSTIterator(None), []
    while i.hasNext(): 
        v.append(i.next())
     
    print(v)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        