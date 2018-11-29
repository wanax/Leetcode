'''
Xiaochi Ma
2018-11-26
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
         

class Solution(object):
    
    def hasCycle(self, head):
        
        if not head:
            return False
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast.val == slow.val:
                return True
        
        return False
    
    def loop(self, head):
        
        if not head:
            return None
        
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast and fast.val == slow.val:
                return fast
        
        return None
    
    def detectCycle(self, head):
        
        if not head:
            return None
        
        fast = self.loop(head)
        if not fast:
            return None
        
        slow = head
        while fast.val != slow.val:
            fast = fast.next
            slow = slow.next
        
        return fast
    
    def insertionSortList(self, head):
        
        if not head:
            return None
        
        dummy = ListNode(0)
        pre = dummy
        
        cur = head
        ne = None
        while cur:
            ne = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = dummy
            cur = ne
        
        return dummy.next
    
    def merge(self, l1, l2):
        
        dummy = ListNode(0)
        node = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        
        return dummy.next
            
    
    def sortList(self, head):
        
        if not head or not head.next:
            return head
        
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
            
        pre.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.merge(l1, l2)
    
    
if __name__ == '__main__':
    
    l1 = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(5)
    node3 = ListNode(4)
    node4 = ListNode(3)

    l1.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
#    node4.next = node1

    solution = Solution()
    
    print(solution.insertionSortList(l1).val)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    