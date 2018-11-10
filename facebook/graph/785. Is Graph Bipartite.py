'''
Xiaochi Ma
2018-11-09
'''

class Solution:
    
    def dfs(self, graph, colors, v, color):
        colors[v] = color
        for neigh in graph[v]:
            if colors[neigh] == color:
                return False
            if colors[neigh] == 0 and not self.dfs(graph, colors, neigh, -color):
                return False
        return True
    
    def isBipartite(self, graph):
        
        colors = [0] * len(graph)
        
        for v in range(len(graph)):
            if colors[v] == 0:
                tag = self.dfs(graph, colors, v, 1)
                if not tag:
                    return False
        
        return True
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    