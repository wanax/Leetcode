'''
Xiaochi Ma
2018-10-21
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        if len(obstacleGrid) == 0:
            return 0
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        obstacleGrid[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
            else:
                obstacleGrid[i][0] = 0
                
        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]
            else:
                obstacleGrid[0][i] = 0
                
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
                    
        return obstacleGrid[m-1][n-1]

    def minPathSum(self, grid):
        
        if len(grid) == 0:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(1, m):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        
        for i in range(1, n):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        
        return grid[m-1][n-1]
    
    

if __name__ == '__main__':
    
    solution = Solution()
    print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))


































