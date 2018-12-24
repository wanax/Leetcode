'''
Xiaochi Ma
2018-12-19
'''

import heapq

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    
    def order(self, root, target, heap):
        
        if not root:
            return
        
        heapq.heappush(heap, [abs(root.val-target), root.val])
        self.order(root.left, target, heap)
        self.order(root.right, target, heap)
    
    def closestKValues(self, root, target, k):
        
        heap = []
        self.order(root, target, heap)
        
        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
        
        
if __name__ == '__main__':
    
    root = TreeNode(4)
    node1 = TreeNode(2)
    node2 = TreeNode(5)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4

    solution = Solution()
    print(solution.closestKValues(root, 3.714286, 2)) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    