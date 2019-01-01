'''
Xiaochi Ma
2018-12-28
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
import math
class Solution:
    
    def bulbSwitch(self, n):
        return int(math.sqrt(n))
    
    def bulbSwitch1(self, n):
        
        if n == 0:
            return 0
        
        arr = [0] * n
        for step in range(1, n):
            for i in range(step-1, n, step):
                arr[i] += 1
        arr[-1] += 1
        arr = list(filter(lambda x:x%2!=0, arr))
        return len(arr)
    
    def wiggleSort(self, nums):
        for i in range(len(nums)-1):
            if i % 2 == 0:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                elif nums[i] == nums[i+1]:
                    t = i+1
                    while t+1 < len(nums) and nums[t] >= nums[t+1]:
                        t += 1
                    nums[i+1], nums[t+1] = nums[t+1], nums[i+1]
            elif i % 2 == 1:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                elif nums[i] == nums[i+1]:
                    t = i + 1
                    while t+1 < len(nums) and nums[t] <= nums[t+1]:
                        t += 1
                    nums[i+1], nums[t+1] = nums[t+1], nums[i+1]
                    
    def oddEvenList(self, head):
        
        if not head:
            return None
        
        foh = head
        feh = head.next
        if not feh:
            return head
        
        p = feh.next
        feh.next = None
        foh.next = None
        fo = foh
        fe = feh
        i = 0
        while p:
            if i%2 == 0:
                fo.next = p
                fo = fo.next
            elif i%2 == 1:
                fe.next = p
                fe = fe.next
            i += 1
            p = p.next
        fe.next = None
        fo.next = feh
        return foh
    
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
    head = solution.oddEvenList(head)
    while head:
        print(head.val)
        head=head.next
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    