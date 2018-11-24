'''
Xiaochi Ma
2018-11-23
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    
    def bfs(self, root, res, cur):
        
        if not root:
            return
        
        cur.append(root.val)
        
        if not root.left and not root.right:
            res.append(int(''.join(map(str, cur))))
            return
        
        self.bfs(root.left, res, cur[:])
        self.bfs(root.right, res, cur[:])
    
    def sumNumbers(self, root):
        
        if not root:
            return 0
        
        res = []
        self.bfs(root, res, [])
        
        return sum(res)
    
    def dfs(self, board, i, j):
        
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1:
            return
        if board[i][j] == 'X' or board[i][j] == 'N':
            return
        
        if board[i][j] == 'O':
            board[i][j] = 'N'
        self.dfs(board, i-1, j)
        self.dfs(board, i+1, j)
        self.dfs(board, i, j-1)
        self.dfs(board, i, j+1)
    
    def solve(self, board):
        
        if len(board) == 0 or len(board[0]) == 0:
            return board
        
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][len(board[0])-1] == 'O':
                self.dfs(board, i, len(board[0])-1)
                
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                self.dfs(board, 0, i)
            if board[len(board)-1][i] == 'O':
                self.dfs(board, len(board)-1, i)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        
        return board
        
        
if __name__ == '__main__':
    
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(0)
    node3 = TreeNode(5)
    node4 = TreeNode(1)

    
    root.left = node1
#    root.right = node2
#    node1.left = node3
#    node1.right = node4

    
    solution = Solution()
    print(solution.solve([100, 4, 200, 1, 3, 2]))     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    