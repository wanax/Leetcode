'''
Xiaochi Ma
2018-11-12
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def rightSideView(self, root):
        
        dic = {}
        max_depth = -1
        stack = [(root, 0)]
        
        while stack:
            node, depth = stack.pop(0)
            if node is not None:
                max_depth = max(max_depth, depth)
                dic[depth] = node.val
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
                
        return [dic[depth] for depth in range(max_depth + 1)]
    
if __name__ == '__main__':
    
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(5)
    node4 = TreeNode(4)
    
    root.left = node1
    root.right = node2
    node1.right = node3
    node2.right = node4
    
    
    solution = Solution()
    print(solution.rightSideView(root))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    