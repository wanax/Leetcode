'''
Xiaochi Ma
2018-10-22
'''

from queue import Queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        
        if root == None:
            return 0
        
        queue = Queue()
        
        deep = 0
        queue.put(root)
        while not queue.empty():
            deep += 1
            k = queue.qsize()
            for i in range(k):
                node = queue.get()
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
                if node.left == None and node.right == None:
                    return deep
        return -1
    
    def levelOrderBottom(self, root):
        
        if root == None:
            return []
        
        queue = Queue()
        arr = []
        
        queue.put(root)
        arr.insert(0, [root.val])
        
        while not queue.empty():
            k = queue.qsize()
            temp = []
            for i in range(k):
                node = queue.get()
                if node.left:
                    temp.append(node.left.val)
                    queue.put(node.left)
                if node.right:
                    temp.append(node.right.val)
                    queue.put(node.right)
            if len(temp) > 0:
                arr.insert(0, temp)
        
        return arr
    
    def zigzagLevelOrder(self, root):
        
        if root == None:
            return []
        
        queue = Queue()
        arr = []
        
        queue.put(root)
        arr.insert(0, [root.val])
        
        while not queue.empty():
            k = queue.qsize()
            temp = []
            for i in range(k):
                node = queue.get()
                if node.left:
                    temp.append(node.left.val)
                    queue.put(node.left)
                if node.right:
                    temp.append(node.right.val)
                    queue.put(node.right)
            if len(temp) > 0:
                arr.append(temp)
                
        for i in range(0, len(arr)):
            if i % 2 != 0:
                temp = arr[i]
                temp.reverse()
                arr[i] = temp
        return arr
    
    
if __name__ == '__main__':
    
    root = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)
    
    root.left = node1
    root.right = node2
    node2.left = node3
    node1.right = node4
    
    solution = Solution()
    print(solution.zigzagLevelOrder(root))     
    
    



