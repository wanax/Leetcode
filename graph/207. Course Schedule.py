'''
Xiaochi Ma
2018-12-06
'''

class Solution(object):
    
    def canFinish(self, numCourses, prerequisites):
        
        dic = {}
        for cour in prerequisites:
            cours = dic.get(cour[0], [])
            cours.append(cour[1])
            dic[cour[0]] = cours
            
        for i in range(numCourses):
            vis = []
            if i in dic:
                vis.append(i)
                stack = dic[i]
                while stack:
                    n = stack.pop()
                    if n in vis:
                        return False
                    if n in dic:
                        vis.append(n)
                        for m in dic[n]:
                            if m not in stack:
                                stack.append(m)
        return True
    
    def findOrder(self, numCourses, prerequisites):
        
        inDegree = {}
        preMap = {}
        for pair in prerequisites:
            take = pair[0]
            pre = pair[1]
            inDegree[take] = inDegree.get(take, 0) + 1
            arr = preMap.get(pre, [])
            arr.append(take)
            preMap[pre] = arr
            
        order = []
        q = []
        for i in range(numCourses):
            if i not in inDegree:
                q.append(i)
        while q:
            k = len(q)
            for i in range(k):
                cour = q.pop(0)
                order.append(cour)
                if cour in preMap:
                    canTakes = preMap[cour]
                    for c in canTakes:
                        inDegree[c] -= 1
                        if inDegree[c] == 0:
                            q.append(c)
        for key, val in enumerate(inDegree):
            if val == 0 and key not in order:
                order.append(key)
        if len(order) < numCourses:
            return []
        return order
    
    
if __name__ == '__main__':
    
    solution = Solution()
#    print(solution.canFinish(2, [[1,0]]))
#    print(solution.canFinish(2, [[1,0],[0,1]]))
#    print(solution.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]))
#    print(solution.canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]))
    print(solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    