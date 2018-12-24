'''
Xiaochi Ma
2018-12-19
'''

class Solution(object):
    
    def buildGraph(self, words):
        
        vis = [-1 for i in range(26)]
        dic = {}
        for i in range(len(words)-1):
            
            cur = words[i]
            ne = words[i+1]
            
            for c in cur:
                vis[ord(c)-ord('a')] = 0
            for c in ne:
                vis[ord(c)-ord('a')] = 0
            
            l = min(len(cur), len(ne))
            for j in range(l):
                arr = dic.get(ord(cur[j])-ord('a'), [])
                if cur[j] != ne[j] and ord(cur[j])-ord('a') not in arr:
                    arr.append(ord(ne[j])-ord('a'))
                    dic[ord(cur[j])-ord('a')] = arr
                    break
                    
        return vis, dic
    
    def dfs(self, vis, i, res, dic):
        
        if vis[i] == 1:
            return False
        
        if i not in dic and vis[i] == 0:
            res.append(chr(i+ord('a')))
            vis[i] = 2
            return True
        
        vis[i] = 1
        ne = dic[i]
        for j in ne:
            if vis[j] == 1:
                return False
            if vis[j] == 0:
                if not self.dfs(vis, j, res, dic):
                    return False
        
        vis[i] = 2
        res.append(chr(i+ord('a')))
        return True
    
    def alienOrder(self, words):
        
        if len(words) == 0:
            return ""
        
        if len(words) == 1:
            return words[0]
        
        n = 26
        vis, dic = self.buildGraph(words)
        
        res = []
        for i in range(n):
            if vis[i] == 0:
                if not self.dfs(vis, i, res, dic):
                    return ""

        return "".join(res[::-1])
    
if __name__ == '__main__':
    
    solution = Solution()
#    print(solution.alienOrder([
#                              "wrt",
#                              "wrf",
#                              "er",
#                              "ett",
#                              "rftt"
#                            ])) 
#    
#    print(solution.alienOrder([
#  "z",
#  "x"
#])) 
#
#    print(solution.alienOrder([
#  "z",
#  "x",
#  "z"
#] )) 
#    print(solution.alienOrder(["wrt","wrf","er","ett","rftt","te"])) 
    print(solution.alienOrder(["wnlb"])) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    