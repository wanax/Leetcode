'''
Xiaochi Ma
2018-12-15
'''

class Vector2D(object):

    def __init__(self, vec2d):
        
        self.arr = []
        for i in range(len(vec2d)):
            j = 0
            while j < len(vec2d[i]):
                self.arr.append(vec2d[i][j])
                j += 1
        

    def next(self):
        return self.arr.pop(0)
        

    def hasNext(self):
        return True if len(self.arr) > 0 else False
        
if __name__ == '__main__':
    
    i, v = Vector2D([[1,2],[3], [4,5,6]]), []
    
    while i.hasNext(): v.append(i.next())
    print(v)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    