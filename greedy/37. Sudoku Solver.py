'''
Xiaochi Ma
2018-10-26
'''

class Solution:
    
    def isValid(self, board, row, col, num):
        
        for i in range(9):
            if str(num) == board[row][i] or str(num) == board[i][col]:
                return False
        
        row_begin = row//3*3
        col_begin = col//3*3
        for i in range(3):
            for j in range(3):
                if str(num) == board[row_begin+i][col_begin+j]:
                    return False
        return True
    
    def solveBacktracking(self, board, row, col):
        
        while row < 9 and col < 9:
            if board[row][col] == '.':
                break
            if col == 8:
                col = 0
                row += 1
            else:
                col += 1
        if row >= 9:
            return board
        nextRow = row + col//8
        nextCol = (col + 1)%9
        
        for num in range(1, 10):
            if self.isValid(board, row, col, num):
                board[row][col] = str(num)
                res = self.solveBacktracking(board, nextRow, nextCol)
                if res:
                    return board
                board[row][col] = '.'
        
        return False
    
    def solveSudoku(self, board):
        
        return self.solveBacktracking(board, 0, 0)
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    