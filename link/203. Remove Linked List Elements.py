'''
Xiaochi Ma
2018-12-06
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return
        p1 = head
        p2 = head.next
        while p1 and p1.val == val:
            p1.next = None
            p1 = p2
            if p2:
                p2 = p2.next
            else:
                p2 = None
            head = p1
        while p1 and p2:
            while p2.val == val:
                p2 = p2.next
                p1.next = p2
            p1 = p2
            if p2:
                p2 = p2.next
            else:
                p2 = None
        return head
    
    def reverseList(self, head):
        
        if not head:
            return None
        
        p1 = head
        p2 = head.next
        
        p1.next = None
        
        while p1 and p2:
            t = p1
            p1 = p2
            p2 = p2.next
            p1.next = t
        
        return p1
    
if __name__ == '__main__':
    
    l1 = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
#    node5 = ListNode(5)
#    node6 = ListNode(6)
    
    l1.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
#    node4.next = node5
#    node5.next = node6
    
    solution = Solution()
    l1 = solution.reverseList(l1)
    
    node = l1
    while node:
        print(node.val)
        node = node.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        