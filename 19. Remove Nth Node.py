'''
Xiaochi Ma
2018-10-18
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        
        node = head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        
        target = length - n + 1
        
        node = head
        while target-2 > 0:
            target -= 1
            node = node.next
        
        removeNode = node.next
        node.next = removeNode.next
        
        return head
        
        
if __name__ == '__main__':
    
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    solution = Solution()
    head = solution.removeNthFromEnd(head, 2)
    
    node = head
    while node:
        print(node.val)
        node = node.next
        




























