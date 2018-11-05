'''
Xiaochi Ma
2018-10-26
'''

class Solution:
    def isValidSudoku(self, board):
        
        row_assert = [{} for i in range(9)]
        col_assert = [{} for i in range(9)]
        block_assert = [{} for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char in row_assert[i] or char in col_assert[j] or char in block_assert[(i//3)*3+j//3]:
                    return False
                else:
                    if char != '.':
                        row_assert[i][char] = 1
                        col_assert[j][char] = 1
                        block_assert[(i//3)*3+j//3][char] = 1
        return True
        

if __name__ == '__main__':
    
    solution = Solution()
    print(solution.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))
    






























