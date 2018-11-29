'''
Xiaochi Ma
2018-11-24
'''

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    
    def cloneGraph(self, node):
        
        if not node:
            return None
        
        nh = UndirectedGraphNode(node.label)
        visited = {node:nh}
        stack = []
        stack.append(node)
        while stack:
            n = stack.pop(0)
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    ncopy = UndirectedGraphNode(neighbor.label)
                    visited[neighbor] = ncopy
                    visited[n].neighbors.append(ncopy)
                    stack.append(neighbor)
                else:
                    visited[n].neighbors.append(visited[neighbor])
                    
        return nh
    
    
if __name__ == '__main__':
    
    node = UndirectedGraphNode(0)
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    
    node.neighbors = [node1, node2]
    node1.neighbors = [node2]
    node2.neighbors = [node2]
    
    solution = Solution()
    print(solution.cloneGraph(node))   