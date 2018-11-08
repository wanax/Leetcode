'''
Xiaochi Ma
2018-10-31
'''

class Solution:
    def maxProfit(self, prices):
        
        max_pro = 0
        min_pri = 2**31 -1
        
        for i in range(len(prices)):
            
            if prices[i] < min_pri:
                min_pri = prices[i]
            elif prices[i] - min_pri > max_pro:
                max_pro = prices[i] - min_pri
        
        return max_pro
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.maxProfit([7,6,4,3,1]))