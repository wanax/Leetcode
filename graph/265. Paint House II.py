'''
Xiaochi Ma
2018-12-16
'''

class Solution(object):
    
    def minCostII(self, costs):
        
        if len(costs) == 0:
            return 0
        
        dp = [costs[0][i] for i in range(len(costs[0]))]
        
        for i in range(1, len(costs)):
            temp = []
            for j in range(len(costs[0])):
                l, r = 999, 999
                if len(dp[:j]) > 0:
                    l = min(dp[:j])
                if len(dp[j+1:]) > 0:
                    r = min(dp[j+1:])
                temp.append(costs[i][j] + min(l, r))
            dp = temp
        
        return min(dp)
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.minCostII([[19,3,18,4,13,1,12,6,3,12,3,3,9],
                              [11,5,9,16,2,19,15,10,13,20,15,2,13],
                              [19,6,18,7,6,10,11,13,8,19,4,14,18],
                              [3,18,18,9,3,6,18,11,7,4,13,3,12]]))