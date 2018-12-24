'''
Xiaochi Ma
2018-12-24
'''

class Solution:
    
    def back(self, res, cur, s):
        
        if len(s) == 0:
            res.append(cur[:])
            return
        
        if len(cur) == 0 or len(cur) == 1:
            for i in range(len(s)):
                if len(cur) == 0:
                    if len(s[:i+1]) > 1 and s[:i+1].startswith('0'):
                        return
                    cur.append(s[:i+1])
                    self.back(res, cur, s[i+1:])
                    cur.pop()
                elif len(cur) == 1:
                    pre = int(cur[-1])
                    cu = int(s[:i+1])
                    if len(s[:i+1]) > 1 and s[:i+1].startswith('0'):
                        return
                    t = str(pre+cu)
                    if s[i+1:].startswith(t):
                        cur.append(s[:i+1])
                        cur.append(s[i+1:i+1+len(t)])
                        self.back(res, cur, s[i+1+len(t):])
                        cur.pop()
                        cur.pop()
        else:
            p1 = int(cur[-1])
            p2 = int(cur[-2])
            t = str(p1 + p2)
            if s.startswith(t):
                cur.append(s[:len(t)])
                self.back(res, cur, s[len(t):])
                cur.pop()
            else:
                return
            
    def dfs(self, s, path):
        if len(path) >= 3 and path[-3]+path[-2] != path[-1]:
            return False
        if not s and len(path) >= 3:
            return True
        for i in range(len(s)):
            cur = s[:i+1]
            if len(cur) > 1 and cur[0] == '0':
                continue
            if self.dfs(s[i+1:], path+[int(cur)]):
                return True
    
    def isAdditiveNumber(self, num):
        
#        if len(num) == 1:
#            return False
#        
#        res = []
#        self.back(res, [], num)
#        
#        tag = False
#        for item in res:
#            if len(item) > 1:
#                tag = True
        
        return self.dfs(num, [])


    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.isAdditiveNumber("12122436")) 
    
    
    
    
    
    
    
    
    
    
    
    