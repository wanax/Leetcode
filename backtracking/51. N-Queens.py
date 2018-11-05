'''
Xiaochi Ma
2018-10-30
'''

class Solution:
    
    def addSolution(self, res, queens):
        
        result = []
        for i in range(len(queens)):
            line = ''
            for j in range(len(queens)):
                if j == queens[i]:
                    line += 'Q'
                else:
                    line += '.'
            result.append(line)
        res.append(result)
        
        return res
    
    def isValid(self, queens, pos):
        
        for i in range(pos):
            if queens[i] == queens[pos]:
                return False
        for i in range(pos):
            if abs(queens[i] - queens[pos]) == abs(i - pos):
                return False
        return True
    
    def solveBacktracking(self, res, queens, pos):
        
        if len(queens) == pos:
            self.addSolution(res, queens)
            return
            
        for i in range(len(queens)):
            queens[pos] = i
            if self.isValid(queens, pos):
                self.solveBacktracking(res, queens, pos+1)
        
        return 0
    
    def totalNQueens(self, n):
        
        res = []
        queens = [0 for i in range(n)]
        self.solveBacktracking(res, queens, 0)
        return res


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.totalNQueens(4))




















