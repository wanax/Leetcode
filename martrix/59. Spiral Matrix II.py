'''
Xiaochi Ma
2018-11-14
'''

class Solution:
    
    def generateMatrix(self, n):
        
        if n == 0:
            return []
        
        res = [[0 for i in range(n)] for j in range(n)]
        
        rowB = 0
        rowE = n-1
        colB = 0
        colE = n-1
        
        k = 1
        while k <= n**2:
            
            for i in range(colB, colE+1):
                res[rowB][i] = k
                k += 1
            rowB += 1
            
            for i in range(rowB, rowE+1):
                res[i][colE] = k
                k += 1
            colE -= 1
            
            if colB < colE:
                for i in range(colE, colB-1, -1):
                    res[rowE][i] = k
                    k += 1
            rowE -= 1
            
            if rowB <= rowE:
                for i in range(rowE, rowB-1, -1):
                    res[i][colB] = k
                    k += 1
            colB += 1
            
        return res


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.generateMatrix(2))

































