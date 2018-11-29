'''
Xiaochi Ma
2018-11-28
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = -2**31
        

    def push(self, x):
        self.min = min(x, self.min)
        self.stack.append(x)
        

    def pop(self):
        if self.stack:
            return self.stack.pop()
        

    def top(self):
        if self.stack:
            return self.stack[-1]
        

    def getMin(self):
        self.min


