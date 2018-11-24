'''
Xiaochi Ma
2018-11-17
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
         
class Solution:
    
    def deleteDuplicates2(self, head):
        
        if head is None:
            return None
        
        p1 = head
        p2 = head.next
        
        while p2:
            if p1.val == p2.val:
                p1.next = p2.next
                if p1:
                    p2 = p1.next
                else:
                    p2 = None
            else:
                p1 = p2
                p2 = p2.next
        
        return head
    
    def deleteDuplicates(self, head):
        
        if head is None:
            return None
        
        dummy  = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next is not None and p.next.next is not None:
            if p.next.val == p.next.next.val:
                same = p.next.val
                while p.next is not None and p.next.val == same:
                    p.next = p.next.next
            else:
                p = p.next
        
        return dummy.next
    
    def partition(self, head, x):
        
        if head is None:
            return None
        
        smallH = ListNode(0)
        bigH = ListNode(0)
        
        small = smallH
        big = bigH
        
        while head:
            temp = ListNode(head.val)
            if temp.val < x:
                small.next = temp
                small = small.next
            else:
                big.next = temp
                big = big.next
            head = head.next
        small.next = bigH.next
        return smallH.next

    
if __name__ == '__main__':
    
    l1 = ListNode(1)
    node1 = ListNode(4)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node4 = ListNode(5)
    node5 = ListNode(2)


    l1.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    
    solution = Solution()
    
    head = solution.partition(l1, 3)
    
    node = head
    while node:
        print(node.val)
        node = node.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        