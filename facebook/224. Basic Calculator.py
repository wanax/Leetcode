'''
Xiaochi Ma
2018-11-09
'''

class Solution:
    
    def op(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
    
    def calculate(self, s):
        
        s = s.strip()
        
        if len(s) == 1:
            return int(s)
        
        pre = -1
        ops = set(['+', '-'])
        op = ''
        stack = []
        res = 0
        for c in s:
            if c == ' ' or c == '(' or c == ')':
                continue
            elif c in ops:
                pre = int(stack.pop(0))
                op = c
            elif pre == -1:
                stack.insert(0, int(c))
            else:
                num = int(c)
                res = (self.op(pre, num, op))
                pre = -1
                op = ''
                stack.insert(0, res)
                
        num = stack.pop(0)
        if num > res:
            return num
        else:
            return res
    
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.calculate("2147483647"))
    
    
    
    
    
    
    
    
    
    