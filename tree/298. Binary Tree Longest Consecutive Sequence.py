'''
Xiaochi Ma
2018-12-23
'''
from heapq import *
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    
    def __init__(self):
        self.max = 0
    
    def helper(self, root, p):
        
        if not root:
            return 0
        
        self.max = max(self.max, 1)
        
        left = self.helper(root.left, root.val)
        right = self.helper(root.right, root.val)
        
        if p!= -10 and root.val == p+1:
            res = max(left, right) + 1
            self.max = max(self.max, res+1)
            return res
        else:
            self.max = max(self.max, left, right)
            return 0
    
    def longestConsecutive(self, root):
        
        if not root:
            return 0
        self.helper(root, -10)
        
        return self.max
    
    def getHint(self, secret, guess):
        
        dic = {}
        for i in secret:
            dic[i] = dic.get(i, 0) + 1
        
        count = 0
        for i in guess:
            if i in dic:
                dic[i] -= 1
                count += 1
                if dic[i] == 0:
                    dic.pop(i)
        count1 = 0        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                count1 += 1
                count -= 1
        
        return "{}A{}B".format(count1, count)
    
if __name__ == '__main__':
    
    arr = []
    heappush(arr, 3)
    heappush(arr, 4)
    heappush(arr, 1)
    heappush(arr, 2)
    
    print(arr[3])

#    solution = Solution()
#    print(solution.getHint("1807", "7810")) 
#    
#    root = TreeNode(1)
#    node1 = TreeNode(3)
#    node2 = TreeNode(2)
#    node3 = TreeNode(4)
#    node4 = TreeNode(5)
#    
#    root.right = node1
#    node1.left = node2
#    node1.right = node3
#    node3.right = node4
    
#    root = TreeNode(2)
#    node1 = TreeNode(3)
#    node2 = TreeNode(2)
#    node3 = TreeNode(1)
#    
#    root.right = node1
#    node1.left = node2
#    node2.left = node3
    
#    root = TreeNode(0)
#    node1 = TreeNode(0)
#    node2 = TreeNode(1)
#    node3 = TreeNode(2)
    
#    root.right = node1
#    node1.right = node2
#    node2.right = node3
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    