'''
Xiaochi Ma
2018-12-11
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    
    def isPalindrome(self, head):
        
        if not head:
            return False
        if not head.next:
            return True
        
        count = 0
        p = head
        while p:
            count += 1
            p = p.next
        
        s = head
        f = head.next
        
        while f and f.next and f.next.next:
            s = s.next
            f = f.next.next
            
        bhalf = None
        if count % 2 == 0:
            bhalf = s.next
        else:
            bhalf = s.next.next
        s.next = None
        
        pre = None
        cur = head
        while cur:
            t = cur
            cur = cur.next
            t.next = pre
            pre = t
        
        prehalf = pre
        p1 = prehalf
        p2 = bhalf
        while p1 and p2:
            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                break
        
        if not p1 and not p2:
            return True
        
        return False
    
if __name__ == '__main__':
    
    l1 = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(2)
    node3 = ListNode(3)
    
    l1.next = node1
    node1.next = node2
    node2.next = node3
    
    solution = Solution()
    print(solution.isPalindrome(l1))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    