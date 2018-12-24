'''
Xiaochi Ma
2018-12-24
'''

class Solution:
    
    def __init__(self):
        self.left = 2**32
        self.right = 0
        self.top = 2**32
        self.bottom = 0
        
    def bfs(self, image, x, y):
        
        if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
            return
        
        if image[x][y] == '0' or image[x][y] == '*':
            return
        else:
            image[x][y] = '*'
            self.left = min(self.left, y)
            self.right = max(self.right, y)
            self.top = min(self.top, x)
            self.bottom = max(self.bottom, x)
            
            vecs = [[-1,0],[1,0],[0,-1],[0,1]]
            for vec in vecs:
                self.bfs(image, x+vec[0], y+vec[1])
    
    def minArea(self, image, x, y):
        
        for row in range(len(image)):
            image[row] = list(image[row])
        
        self.bfs(image, x, y)
        area = (self.right-self.left+1)*(self.bottom-self.top+1)
        
        return area
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.minArea([
                              "0010",
                              "0110",
                              "0100"
                            ], 0, 2)) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    