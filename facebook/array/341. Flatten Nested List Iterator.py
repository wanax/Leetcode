'''
Xiaochi Ma
2018-11-05
'''

class NestedIterator(object):

    def __init__(self, nestedList):
        self.res = []
        for item in nestedList:
            if isinstance(item, int):
                self.res.append(item)
            else:
                q = []
                q.append(item)
                while len(q) > 0:
                    temps = q.pop(0)
                    for n in temps:
                        if isinstance(n, int):
                            self.res.append(n)
                        else:
                            q.append(n)
                            
    def flatten(self, nestList):
        for item in nestList:
            if isinstance(item, int):
                self.res.append(item)
            else:
                self.flatten(item)

    def next(self):
        
        return self.res.pop(0)
        

    def hasNext(self):
        return True if len(self.res) > 0 else False
    
if __name__ == '__main__':
    
    nestedList = [[1,1],2,[1,1]]
    i, v = NestedIterator(nestedList), []
    while i.hasNext(): 
        v.append(i.next())
    print(v)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    