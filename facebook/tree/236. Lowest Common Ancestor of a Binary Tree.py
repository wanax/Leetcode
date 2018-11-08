'''
Xiaochi Ma
2018-11-06
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    
    def bfs(self, root, res, cur, p, q):
        
        if root is None:
            return
        
        cur.append(root.val)
        if len(cur) > 0 and (cur[-1] == p or cur[-1] == q):
            vs = res.get(cur[-1], [])
            vs.append(cur[:])
            res[cur[-1]] = vs
            return
        
        if root.left:
            self.bfs(root.left, res, cur[:], p, q)
        if root.right:
            self.bfs(root.right, res, cur[:], p, q)
            
    
    def lowestCommonAncestor2(self, root, p, q):
        
        if root is None:
            return 0
        
        res = {}
        self.bfs(root, res, [], p, q)
        
        if q not in res:
            return p
        elif p not in res:
            return q
        
        list1 = res[q][0]
        list2 = res[p][0]
        
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] != list2[j]:
                break
            i += 1
            j += 1
        return list1[i-1]
    
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parent = {root: None}
        while len(stack) > 0 and (p not in parent or q not in parent):
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q
    
if __name__ == '__main__':
    
    root = TreeNode(3)
    node1 = TreeNode(5)
    node2 = TreeNode(1)
    node3 = TreeNode(6)
    node4 = TreeNode(2)
    node5 = TreeNode(0)
    node6 = TreeNode(8)
    node7 = TreeNode(7)
    node8 = TreeNode(4)
    
    root.left = node1
    root.right = node2
    
    node1.left = node3
    node1.right = node4
    node4.left = node7
    node4.right = node8
    
    node2.left = node5
    node2.right = node6
    
    solution = Solution()
    print(solution.lowestCommonAncestor(root, 5, 1))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    