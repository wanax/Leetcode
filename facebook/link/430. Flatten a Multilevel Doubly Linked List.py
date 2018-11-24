'''
Xiaochi Ma
2018-11-12
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.child = None

class Solution(object):
    
    def flatten(self, head):
        
        node = head
        while node is not None:
            if node.child is None:
                node = node.next
                continue
            child = self.flatten(node.child)
            childT = child
            while childT.next is not None:
                childT = childT.next
            child.prev = node
            childT.next = node.next
            if node.next:
                node.next.prev = childT
            node.next = child
            node = childT.next
        
        return head


if __name__ == '__main__':
    
    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)
    
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    
    node2.prev = head
    node3.prev = node2
    node4.prev = node3
    node5.prev = node4
    node6.prev = node5
    
    node7.next = node8
    node8.next = node9
    node9.next = node10
    
    node8.prev = node7
    node9.prev = node8
    node10.prev = node9
    
    node11.next = node12
    node12.prev = node11
    
    node3.child = node7
    node8.child = node11
    
    solution = Solution()
    head = solution.flatten(head)
    
    node = head
    while node is not None:
        print(node.val)
        node = node.next
#        
#    node = node6
#    while node is not None:
#        print(node.val)
#        node = node.prev

























