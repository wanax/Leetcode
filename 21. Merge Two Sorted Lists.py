'''
Xiaochi Ma
2018-10-18
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    
    def mergeTwoLists(self, l1, l2):
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        num = l2
        sendAgain = l1
        if l1.val < l2.val:
            num = l1
            sendAgain = l2
        newNode = ListNode(num.val)
        newNode.next = self.mergeTwoLists(sendAgain, num.next)
        return newNode
    
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans

if __name__ == '__main__':
    
    l1 = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(4)
    
    l2 = ListNode(1)
    node11 = ListNode(3)
    node21 = ListNode(4)


    l1.next = node1
    node1.next = node2
    
    l2.next = node11
    node11.next = node21
    
    
    solution = Solution()
    
    print(solution.generateParenthesis(4))
    
    head = solution.mergeTwoLists(l1, l2)
    
    node = head
    while node:
        print(node.val)
        node = node.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                