'''
Xiaochi Ma
2018-11-18
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
         
         
class Solution:
    
    def reverseBetween(self, head, m, n):
        
        if head is None:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        
        p = dummy
        q = dummy.next
        for i in range(1, m):
            if q:
                p = p.next
                q = q.next
        
        l = q
        pre = p
        
        p = dummy
        for i in range(0, n):
            if p:
                p = p.next
        r = p
        
        tail = r.next
        end = tail
        
        p = l
        temp = p
        while p!= tail:
            temp = p
            p = p.next
            temp.next = end
            end = temp
        
        pre.next = temp
        
        return dummy.next
    
if __name__ == '__main__':
    
    l1 = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)

    l1.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution = Solution()
    
    head = solution.reverseBetween(l1, 2, 4)
    
    node = head
    while node:
        print(node.val)
        node = node.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        