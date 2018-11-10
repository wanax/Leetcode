'''
Xiaochi Ma
2018-11-08
'''

def adjacent(row, col, grid, cur):
        
    nrow = len(grid)
    ncol = len(grid[0])
    
    neighs = []
    if row-1 >= 0:
        if grid[row-1][col] == '1':
            grid[row-1][col] = '*'
            neighs.append([row-1, col])
            cur.append([row-1, col])
    if row+1 < nrow:
        if grid[row+1][col] == '1':
            grid[row+1][col] = '*'
            neighs.append([row+1, col])
            cur.append([row+1, col])
    if col-1 >= 0:
        if grid[row][col-1] == '1':
            grid[row][col-1] = '*'
            neighs.append([row, col-1])
            cur.append([row, col-1])
    if col+1 < ncol:
        if grid[row][col+1] == '1':
            grid[row][col+1] = '*'
            neighs.append([row, col+1])
            cur.append([row, col+1])
    return neighs
    
def bfs(row, col, grid, cur, res):
    
    q = []
    q.append([row, col])
    while len(q) > 0:
        k = len(q)
        for i in range(k):
            node = q.pop(0)
            grid[node[0]][node[1]] = '*'
            neigs = adjacent(node[0], node[1], grid, cur)
            for node in neigs:
                q.append(node)
    res.append(cur)
                
def numOfBlock(grid):
    
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    
    count = 0
    res = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                cur = []
                cur.append([i, j])
                bfs(i, j, grid, cur, res)
    
    return res

def countMatches(grid1, grid2):
    
    n = len(grid1)
    grid_1 = [['0' for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            grid_1[i][j] = grid1[i][j]
            
    m = len(grid2)
    grid_2 = [['0' for i in range(m)] for j in range(m)]

    for i in range(n):
        for j in range(n):
            grid_2[i][j] = grid2[i][j]
    
    res = numOfBlock(grid_1)    
    res2 = numOfBlock(grid_2)
    
    count = 0
    for item in res:
        for item2 in res2:
            if item == item2:
                count += 1
    return count
    
if __name__ == '__main__':
    
    count = countMatches(['001', '011', '100'], 
                         ['001', '011', '101'])

    print(count)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    