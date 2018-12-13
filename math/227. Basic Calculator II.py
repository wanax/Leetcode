'''
Xiaochi Ma
2018-12-09
'''

class Solution(object):
    
    def op(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        elif op == '*':
            return n1 * n2
        elif op == '/':
            return n1//n2
    
    def calculate(self, s):
        
        levels = {'+':0, '-':0, '*':1, '/':1}
        opStack = []
        numStack = []
        
        s = s.strip()
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if s[i] not in levels:
                num = ''
                while i < len(s) and s[i] not in levels and s[i] != ' ':
                    num += s[i]
                    i += 1
                numStack.append(int(num))
            elif s[i] in levels:
                if len(opStack) == 0 or levels[s[i]] > levels[opStack[-1]]:
                    opStack.append(s[i])
                    i += 1
                else:
                    while len(opStack) > 0 and levels[opStack[-1]] >= levels[s[i]]:
                        op = opStack.pop()
                        n2 = numStack.pop()
                        n1 = numStack.pop()
                        num = self.op(n1, n2, op)
                        numStack.append(num)
                    opStack.append(s[i])
                    i += 1
        
        total = 0
        while opStack:
            op = opStack.pop()
            n2 = numStack.pop()
            n1 = numStack.pop()
            num = self.op(n1, n2, op)
            numStack.append(num)
        while numStack:
            total = numStack.pop()
        
        return total
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.calculate("2*3+4"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    