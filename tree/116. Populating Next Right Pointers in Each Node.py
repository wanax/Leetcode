'''
Xiaochi Ma
2018-11-21
'''

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
        
class Solution:
    
    def connect(self, root):
        
        if not root:
            return
        
        queue = []
        queue.append(root)
        while len(queue):
            k = len(queue)
            pre = None
            for i in range(k):
                node = queue.pop(0)
                if pre:
                    pre.next = node
                pre = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            pre = None   
        
        
        return
    
    
if __name__ == '__main__':
    
    root = TreeLinkNode(1)
    node1 = TreeLinkNode(2)
    node2 = TreeLinkNode(3)
    node3 = TreeLinkNode(4)
    node4 = TreeLinkNode(5)
    node5 = TreeLinkNode(6)
    node6 = TreeLinkNode(7)
    
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node3.right = node6

    solution = Solution()
    print(solution.connect(root)) 