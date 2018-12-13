'''
Xiaochi Ma
2018-12-03
'''

class Solution:
    
    def singleMaxProfit(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                res += prices[i] - prices[i-1]
        return res
    
    def maxProfit(self, k, prices):
        
        if len(prices) == 0:
            return 0
        
        if k >= len(prices):
            return self.singleMaxProfit(prices)
        
        local = [0 for i in range(k+1)]
        global_s = [0 for i in range(k+1)]
        
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            for j in range(k, 0, -1):
                local[j] = max(global_s[j-1]+(diff if diff>0 else 0), local[j]+diff)
                global_s[j] = max(local[j], global_s[j])
        
        return global_s[k]
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.maxProfit([3,3,5,0,0,3,1,4]))  