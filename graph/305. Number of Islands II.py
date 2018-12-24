'''
Xiaochi Ma
2018-12-24
'''

class Solution:
    
    def find(self, roots, pos):
        while pos != roots[pos]:
            pos = roots[pos]
        return pos
    
    def numIslands2(self, m, n, positions):
        
        res = []
        if m <= 0 or n <= 0:
            return res
        
        count = 0
        roots = [-1 for i in range(m*n)]
        
        vecs = [[1,0],[-1,0],[0,1],[0,-1]]
        for pos in positions:
            cur = n * pos[0] + pos[1]
            roots[cur] = cur
            count += 1
            
            for vec in vecs:
                x = pos[0] + vec[0]
                y = pos[1] + vec[1]
                ne = n * x + y
                if x < 0 or x >= m or y < 0 or y >= n or roots[ne] == -1:
                    continue
                anOther = self.find(roots, ne)
                if cur != anOther:
                    roots[cur] = anOther
                    cur = anOther
                    count -= 1
            res.append(count)
        
        return res
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.numIslands2(3, 3, [[0,0], [0,1], [1,2], [2,1]])) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    