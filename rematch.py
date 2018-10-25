'''
Xiaochi Ma
2018-10-12
'''

def isEqual(p, q):
    if p == q or p == '.':
        return True
    else:
        return False

class Solution(object):
    def isMatch(self, s, p):
        c = 'None'
        pre = 'None'
        k = 0
        i = 0
        for i in range(len(s)):
            
            if k == len(p):
                return False
                break
            
            t = s[i]
            if p[k] == '*':
                c = pre
            else:
                c = p[k]
                pre = p[k]
                k += 1
            if isEqual(c, t):
                continue
            if k < len(p) and p[k] == '*' and c != t:
                k += 1
                if k < len(p) and isEqual(p[k], t):
                    continue
                else:
                    return False
                    break
            else:
                return False
                break
        if i == len(s) - 1:
            return True

if __name__ == "__main__":
    
    s = "mississippi"
    p = "mis*is*ip*."
    
    solution = Solution()
    print(solution.isMatch(s, p))
        
        
            
        
        











