'''
Xiaochi Ma
2018-11-08
'''

class NumMatrix:

    def __init__(self, matrix):
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return

        sums = [ [ 0 for i in range(len(matrix[0])+1) ] for j in range(len(matrix)) ]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sums[i][j+1] = sums[i][j] + matrix[i][j]
        self.sum = sums
        

    def sumRegion(self, row1, col1, row2, col2):
        
        total = 0
        for i in range(row1, row2+1):
            total += (self.sum[i][col2+1] - self.sum[i][col1])
        
        return total
    
if __name__ == '__main__':
    
    obj = NumMatrix([ [3, 0, 1, 4, 2],
                      [5, 6, 3, 2, 1],
                      [1, 2, 0, 1, 5],
                      [4, 1, 0, 1, 7],
                      [1, 0, 3, 0, 5]])
    
    print(obj.sumRegion(2, 1, 4, 3))