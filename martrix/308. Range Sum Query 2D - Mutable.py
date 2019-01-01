'''
Xiaochi Ma
2018-12-26
'''

class NumMatrix:
    
    def _update(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                left = 0 if i-1<0 else self.sum[i-1][j]
                right = 0 if j-1<0 else self.sum[i][j-1]
                small = 0 if i-1<0 or j-1<0 else self.sum[i-1][j-1]
                self.sum[i][j] = left+right-small+self.matrix[i][j]

    def __init__(self, matrix):
        self.matrix = matrix
        self.sum = [[0] * len(matrix[0]) for i in range(len(matrix))]
        self._update()
        

    def update(self, row, col, val):
        self.matrix[row][col] = val
        self._update()

    def sumRegion(self, row1, col1, row2, col2):
        left = 0 if row1-1<0 else self.sum[row1-1][col2]
        right = 0 if col1-1<0 else self.sum[row2][col1-1]
        small = 0 if row1-1<0 or col1-1<0 else self.sum[row1-1][col1-1]
        res = self.sum[row2][col2] - left - right + small
        return res
        
if __name__ == '__main__':
    
    obj = NumMatrix([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])
#    obj.update(3, 2, 2)
    print(obj.sumRegion(2, 1, 4, 3))
    
    
    
    
    
    
    
    
    
    
    
    
    
    