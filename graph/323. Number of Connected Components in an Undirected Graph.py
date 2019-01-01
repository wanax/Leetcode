'''
Xiaochi Ma
2018-12-28
'''

class Solution:
    
    def countComponents(self, n, edges):
        
        dic = {}
        for i in range(n):
            dic[i] = []
            
        for e in edges:
            dic[e[0]].append(e[1])
            dic[e[1]].append(e[0])
        
        vis = [False for i in range(n)]
        count = 0
        for i in range(n):
            if not vis[i]:
                count += 1
                stack = []
                stack.append(i)
                while stack:
                    root = stack.pop(0)
                    vis[root] = True
                    subs = dic[root]
                    for n in subs:
                        if not vis[n]:
                            stack.append(n)
        
        return count
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.countComponents(5,  [[0, 1], [1, 2], [2, 3], [3, 4]])) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    