'''
Xiaochi Ma
2018-12-28
'''

class Solution:
    
    def dfs(self, path, word, res, i, k):
        
        if i == len(word):
            if k != 0:
                path.append(str(k))
            res.append("".join(path))
            return
        else:
            self.dfs(path[:], word, res, i+1, k+1)
            
            if k != 0:
                path.append(str(k))
            path.append(word[i])
            self.dfs(path, word, res, i+1, 0)
            path.pop()
                
    
    def generateAbbreviations(self, word):
        
        res = []
        self.dfs([], word, res, 0, 0)
        return res
    
    def __init__(self):
        self.min = 2**32
    
    def dfs2(self, coins, amount, count):
        
        if amount > 0 and len(coins) == 0:
            return
        div = amount/coins[0]
        if div+count > self.min:
            return
        if amount%coins[0] == 0:
            self.min = min(self.min, div+count)
            return
        
        if amount == 0:
            self.min = min(self.min, count)
            return

        
        n = amount//coins[0]
        for i in range(n+1):
            self.dfs2(coins[1:], amount-i*coins[0], count+i)
        
    def coinChange(self, coins, amount):
        
        rs = [amount+1] * (amount+1)
        rs[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i-c] + 1)

        if rs[amount] == amount+1:
            return -1
        return rs[amount]
    
#        if amount == 0:
#            return 0
#        if len(coins) == 0:
#            return -1
#        
#        coins.sort(reverse=True)
#        self.dfs2(coins, amount, 0)
#        
#        return int(self.min) if self.min != 2**32 else -1
    
if __name__ == '__main__':
    
    solution = Solution()
#    print(solution.coinChange([1, 2, 5], 11)) 
    print(solution.coinChange([389,46,222,352,4,250], 5343)) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    