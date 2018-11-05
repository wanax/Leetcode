'''
Xiaochi Ma
2018-10-30
'''

class Solution:
    
    def spiralOrder(self, matrix):
        
        if len(matrix) == 0:
            return []
        
        res = []  
        
        rowB = 0
        rowE = len(matrix) - 1
        colB = 0
        colE = len(matrix[0]) - 1
        
        while rowB <= rowE and colB <= colE:
            
            for i in range(colB, colE+1):
                res.append(matrix[rowB][i])
            rowB += 1
            
            for i in range(rowB, rowE+1):
                res.append(matrix[i][colE])
            colE -= 1
            
            if colB < colE:
                for i in range(colE, colB-1, -1):
                    res.append(matrix[rowE][i])
            rowE -= 1
            
            if rowB <= rowE:
                for i in range(rowE, rowB-1, -1):
                    res.append(matrix[i][colB])
            colB += 1
            
        return res


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.spiralOrder([[6,9,7]]))























