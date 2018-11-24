'''
Xiaochi Ma
2018-11-12
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def sortedListToBST(self, head):
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        self.node = head
        return self.convert(0, l-1)
    
    def convert(self, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        l = self.convert(start, mid-1)
        root = TreeNode(self.node.val)
        root.left = l
        self.node = self.node.next 
        root.right = self.convert(mid+1, end)
        return root
    
if __name__ == '__main__':
    
    head = ListNode(-10)
    node2 = ListNode(-3)
    node3 = ListNode(0)
    node4 = ListNode(5)
    node5 = ListNode(9)
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    
    solution = Solution()
    print(solution.sortedListToBST(head))
    
    node = head
    while node:
        print(node.val)
        node = node.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        