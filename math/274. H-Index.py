'''
Xiaochi Ma
2018-10-19
'''

class Solution(object):
    
    def hIndex(self, citations):
        
        if len(citations) == 0:
            return 0
        
        count = 0
        for i in range(len(citations)-1, -1, -1):
            if count < citations[i]:
                count += 1

        
        return count


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.hIndex([0,1,3,5,6]))







