'''
Xiaochi Ma
2018-11-18
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def helper(self, s, e):
        
        if s > e:
            return [None, ]
        
        trees = []
        for i in range(s, e+1):
            
            ls = self.helper(s, i-1)
            rs = self.helper(i+1, e)
            
            for l in ls:
                for r in rs:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    trees.append(root)
        return trees
            
    
    def generateTrees(self, n):
        
        return self.helper(1, n) if n else []
    
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.generateTrees(3))   



































