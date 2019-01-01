'''
Xiaochi Ma
2018-12-29
'''
from collections import deque
class Solution:
    
    def shortestDistance(self, grid):
        
        if not grid or not grid[0]:
            return -1
        
        M, N, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1)
        hit, distsum = [[0] * N for i in range(M)], [[0] * N for i in range(M)]
        
        def bfs(x, y):
            vis = [[False] * N for k in range(M)]
            vis[x][y] = True
            count = 1
            q = deque([(x, y, 0)])
            while q:
                x,y,dist = q.popleft()
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < M and 0 <= j < N and not vis[i][j]:
                        vis[i][j] = True
                        if not grid[i][j]:
                            q.append((i, j, dist + 1))
                            hit[i][j] += 1
                            distsum[i][j] += dist+1
                        elif grid[i][j] == 1:
                            count += 1
            return count == buildings
                    
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    if not bfs(x, y): return -1                
        
        return min([distsum[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hit[i][j] == buildings] or [-1])
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    