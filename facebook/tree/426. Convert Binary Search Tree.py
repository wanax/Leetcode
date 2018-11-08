'''
Xiaochi Ma
2018-11-01
'''

class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def inOrder(self, node, temp):
        
        if node and node.left:
            temp = self.inOrder(node.left, temp)
        
        if node:
            temp.right = node
            node.left = temp
            temp = node
        
        if node and node.right:
            temp = self.inOrder(node.right, temp)
        
        return temp
    
    def treeToDoublyList(self, root):
        
        head = Node(0, None, None)
        temp = head
        
        self.inOrder(root, temp)
        
        node = head.right
        while node and node.right:
            node = node.right
        
        if node:
            node.right = head.right
            head.right.left = node
            
            node = head.right
        
        return head
    
    
if __name__ == '__main__':
    
    root = Node(1, None, None)
    node2 = Node(3, None, None)
    
    node1 = Node(2, root, node2)
    node4 = Node(5, None, None)
    
    node3 = Node(4, node1, node4)
    
    
    solution = Solution()
    head = solution.treeToDoublyList(node3)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    