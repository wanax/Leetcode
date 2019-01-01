'''
Xiaochi Ma
2018-12-26
'''
from functools import reduce
class Solution:
    
    def findMinHeightTrees(self, n, edges):
        
        if len(edges) == 0:
            return [0]
        
        degrees = [0] * n
        graph = {x:[] for x in range(n)}
        for edge in edges:
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        q = [x for x in range(n) if degrees[x] == 1]
        ret = []
        while q:
            temp = []
            ret = q[:]
            for x in q:
                for n in graph[x]:
                    degrees[n] -= 1
                    if degrees[n] == 1:
                        temp.append(n)
            q = temp
        
        return ret
    
    def multiply2(self, A, B):
        
        nrow = len(A)
        ncol = len(B[0])
        
        res = [[0] * ncol for i in range(nrow)]
        for i in range(nrow):
            for j in range(ncol):
                l1 = A[i]
                l2 = []
                for k in range(len(B)):
                    l2.append(B[k][j])
                res[i][j] = reduce(lambda a,b:a+b, [a*b for a, b in zip(l1, l2)])
        
        return res
    
    def multiply(self, A, B):

        new_A = []
        for i in range(len(A)):
            row = []
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    row.append((j, A[i][j]))
            new_A.append(row)

        result = [[0] * len(B[0]) for _ in range(len(A))]
        for i in range(len(new_A)):
            for j in range(len(new_A[i])):
                for k in range(len(B[0])):
                    result[i][k] += new_A[i][j][1] * B[new_A[i][j][0]][k]
        return result
    
    def maxProfit(self, prices):
        
        if len(prices) <= 1:
            return 0
        
        s0 = [0] * len(prices) #cool
        s1 = [0] * len(prices) #buy
        s2 = [0] * len(prices) #sell
        
        s0[0] = 0
        s1[0] = -prices[0]
        s2[0] = 0
        
        for i in range(1, len(prices)):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1]-prices[i])
            s2[i] = s1[i-1] + prices[i] 
        
        return max(s0[len(prices)-1],s1[len(prices)-1],s2[len(prices)-1])
    
if __name__ == '__main__':
    
    solution = Solution()
#    print(solution.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])) 
#    print(solution.findMinHeightTrees(7, [[0, 3], [1, 3], [2, 3],[5, 4],[4, 6],[6, 3]])) 
#    print(solution.multiply([
#                              [ 1, 0, 0],
#                              [-1, 0, 3]
#                            ],[
#                                  [ 7, 0, 0 ],
#                                  [ 0, 0, 0 ],
#                                  [ 0, 0, 1 ]
#                                ])) 
    
    print(solution.maxProfit([1,2,3,0,2])) 
    
#    l1 = [1,2,3]
#    l2 = [3,4,5]
#    print(reduce(lambda a,b:a+b, [a*b for a, b in zip(l1, l2)]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    