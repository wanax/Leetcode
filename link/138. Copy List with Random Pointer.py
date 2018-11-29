'''
Xiaochi Ma
2018-11-25
'''

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    
    def copyRandomList(self, head):
        
        dic = {}
        
        dummy = RandomListNode(0)
        pre = dummy
        p = head
        while p:
            if p not in dic:
                cp = RandomListNode(p.label)
                dic[p] = cp
            if p.next and p.next not in dic:
                cnextp = RandomListNode(p.next.label)
                dic[p.next] = cnextp
            if p.random and p.random not in dic:
                cranp = RandomListNode(p.random.label)
                dic[p.random] = cranp
            copyp = dic[p]
            if p.next in dic:
                copyp.next = dic[p.next]
            if p.random in dic:
                copyp.random = dic[p.random]
            pre.next = copyp
            pre = copyp
            p = p.next
        
        return dummy.next
        
        
if __name__ == '__main__':
    
    l1 = RandomListNode(1)
    node1 = RandomListNode(2)
    node2 = RandomListNode(3)
    node3 = RandomListNode(4)
    node4 = RandomListNode(5)
    
    l1.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    l1.random = node2
    node1.random = node4
    node4.random = node3
    
    solution = Solution()
    print(solution.copyRandomList(l1))