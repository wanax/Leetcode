'''
Xiaochi Ma
2018-11-06
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    
    def bfs(self, root, dic):
        q = []
        q.append([root, 0])
        while len(q) > 0:
            k = len(q)
            for i in range(k):
                comb = q.pop(0)
                vs = dic.get(comb[1], [])
                vs.append(comb[0].val)
                dic[comb[1]] = vs
                if comb[0].left:
                    q.append([comb[0].left, comb[1]-1])
                if comb[0].right:
                    q.append([comb[0].right, comb[1]+1])

    
    def verticalOrder(self, root):
        
        if root is None:
            return []
        
        dic = {}
        self.bfs(root, dic)
        
        keys = list(dic.keys())
        keys.sort()
        res = []
        for key in keys:
            res.append(dic[key])
        
        return res
    
    

if __name__ == '__main__':
    
    root = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(8)
    node3 = TreeNode(4)
    node4 = TreeNode(0)
    node5 = TreeNode(1)
    node6 = TreeNode(7)
    node7 = TreeNode(2)
    node8 = TreeNode(5)
    
    root.left = node1
    root.right = node2
    
    node1.left = node3
    node1.right = node4
    node4.right = node7
    
    node2.left = node5
    node2.right = node6
    node5.left = node8
    
    solution = Solution()
    print(solution.verticalOrder(root))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    