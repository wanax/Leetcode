'''
Xiaochi Ma
2018-10-18
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    
    def countList(self, head):
        num = 0
        node = head
        while node is not None:
            num += 1
            node = node.next
        return num
    
    def minNode(self, nodes):
        
        minNode = ListNode(999)
        
        index = 0
        for i in range(len(nodes)):
            if nodes[i].val < minNode.val:
                minNode = nodes[i]
                index = i
                
        returnNode = ListNode(minNode.val)
        
        head = nodes[index]
        head = head.next
        
        if head is None:
            nodes.pop(index)
        else:
            nodes[index] = head
        
        return returnNode
    
    def mergeKLists(self, lists):
        
        lists = [head for head in lists if head != None]
        
        total = 0
        for node in lists:
            total += self.countList(node)
        
        head = ListNode(-1)
        node = head
        for i in range(total):
            minNode = self.minNode(lists)
            node.next = minNode
            node = node.next
        
        return head.next
    
    
if __name__ == '__main__':
    
    l1 = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(5)
    
    l2 = ListNode(1)
    node21 = ListNode(3)
    node22 = ListNode(4)
    node23 = ListNode(8)
    
    l3 = ListNode(0)
    node31 = ListNode(5)

    l1.next = node1
    node1.next = node2
    node2.next = node3
    
    l2.next = node21
    node21.next = node22
    node22.next = node23
    
    l3.next = node31
    
    solution = Solution()
    
    head = solution.mergeKLists([l1, l2, l3])
    
    node = head
    while node:
        print(node.val)
        node = node.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        