'''
Xiaochi Ma
2018-11-12
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def reorderList(self, head):
        
        if head is None:
            return None
        
        nodes = []
        tmp = head
        length = 0
        
        while tmp:
            nodes.append(tmp)
            tmp = tmp.next
            length += 1
            
        for i in range(length//2):
            nodes[i].next = nodes[length-i-1]
            nodes[length-i-1].next = nodes[i+1]
        nodes[length//2].next = None
        return head
    
    
if __name__ == '__main__':
    
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    
    solution = Solution()
    print(solution.reorderList(head))
    
    node = head
    while node:
        print(node.val)
        node = node.next
    
    
    
    
    
    
    
    
    