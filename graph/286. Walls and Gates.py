'''
Xiaochi Ma
2018-12-21
'''

class Solution(object):
    
    
    def wallsAndGates(self, rooms):
        
        inf = 2**31 - 1
        
        begins = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    begins.append([i,j])
                    
        step = 1
        vecs = [[1,0], [-1,0], [0,1], [0,-1]]
        while begins:
            k = len(begins)
            for i in range(k):
                cur = begins.pop(0)
                ns = [[cur[0]+vec[0], cur[1]+vec[1]] for vec in vecs]
                for n in ns:
                    if n[0] >= 0 and n[0] < len(rooms)\
                    and n[1] >= 0 and n[1] < len(rooms[0]):
                        if rooms[n[0]][n[1]] == inf:
                            begins.append([n[0], n[1]])
                            rooms[n[0]][n[1]] = step
            step += 1
        
        return rooms
    
    def findDuplicate(self, nums):
        
        for i in range(len(nums)):
            if i == nums[i] - 1:
                continue
            else:
                while nums[i] - 1 != i:
                    if nums[i] == nums[nums[i]-1]:
                        return nums[i]
                    self.swap(i, nums[i]-1, nums)
        
        return nums[-1]
    
    def swap(self, i, j, nums):
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t
    
    
if __name__ == '__main__':
    


    solution = Solution()
#    print(solution.wallsAndGates([[2147483647,-1,0,2147483647],
#                                  [2147483647,2147483647,2147483647,-1],
#                                  [2147483647,-1,2147483647,-1],
#                                  [0,-1,2147483647,2147483647]])) 
    print(solution.findDuplicate([3,1,3,4,2]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    