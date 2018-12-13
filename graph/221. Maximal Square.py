'''
Xiaochi Ma
2018-12-08
'''

class Solution(object):
    
    def maximalSquare2(self, matrix):
        
        if len(matrix) == 0:
            return 0
        
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        area = 0
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == '1':
                    sides = range(1, min(nrow-i, ncol-j)+1)
                    for side in sides:
                        valid = []
                        for m in range(i, i+side):
                            for n in range(j, j+side):
                                valid.append([m, n])
                        tag = True
                        for pos in valid:
                            if matrix[pos[0]][pos[1]] == '0':
                                tag = False
                                break
                        if tag:
                            area = max(side**2, area)
        
        return area
    
    def maximalSquare(self, matrix):
        
        if len(matrix) == 0:
            return 0
        
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        dp = [[0 for i in range(ncol)] for j in range(nrow)]
        tag = 0
        for i in range(nrow):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                tag = 1
        for i in range(ncol):
            if matrix[0][i] == '1':
                dp[0][i] = 1
                tag = 1
        
        area = tag
        for i in range(1, nrow):
            for j in range(1, ncol):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    area = max(dp[i][j]**2, area)
        
        return area
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.maximalSquare([["0","0","0","0","0"],
                                  ["1","1","0","0","0"],
                                  ["1","0","0","0","0"],
                                  ["0","0","0","0","0"]]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    