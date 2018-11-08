'''
Xiaochi Ma
2018-11-06
'''
from collections import defaultdict
class Solution:
    
    def validTree(self, n, edges):
        
        if n != len(edges) + 1:
            return False
        
        adList = defaultdict(list)
        
        for edge in edges:
            adList[edge[0]].append(edge[1])
            adList[edge[1]].append(edge[0])
            
        explored = set([])
        stack = [0]
        parent = [-1 for _ in range(n)]
        
        while len(stack) > 0:
            node = stack.pop(0)
            explored.add(node)
            for v in adList[node]:
                if v in explored and parent[node] != v:
                    return False
                if v not in explored:
                    stack.append(v)
                    parent[v] = node
        
        return len(explored) == n
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    