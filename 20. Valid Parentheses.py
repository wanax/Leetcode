'''
Xiaochi Ma
2018-10-18
'''

class Solution:
    def isValid(self, s):
        
        arr = []
        for c in s:
            if c in ['(', '{', '[']:
                arr.append(c)
            elif c == ')' and len(arr) > 0 and arr[-1] == '(':
                arr.pop()
            elif c == '}' and len(arr) > 0 and arr[-1] == '{':
                arr.pop()
            elif c == ']' and len(arr) > 0 and arr[-1] == '[':
                arr.pop()
            else:
                arr.append(c)
        if len(arr) == 0:
            return True
        else:
            return False
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("{[]}"))
            



























