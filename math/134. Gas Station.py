'''
Xiaochi Ma
2018-11-24
'''

class Solution(object):
    
    def canCompleteCircuit2(self, gas, cost):

        get = False
        for i in range(len(gas)):
            count = 0
            carry = 0
            for j in range(i, i+len(gas)):
                index = j%len(gas)
                carry = (carry + gas[index] - cost[index])
                if carry >= 0:
                    count += 1
                    continue
                else:
                    break
            
            if count >= len(gas):
                get = True
                break
        
        return i if get else -1
    
    def canCompleteCircuit(self, gas, cost):
        
        start, lack, left = 0, 0, 0
        for i in range(len(gas)):
            left += (gas[i] - cost[i])
            if left < 0:
                start = i + 1
                lack += left
                left = 0
        return start if lack+left >= 0 else -1
    
    def candy(self, ratings):
        
        dp = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                dp[i] = dp[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                dp[i] = max(dp[i], dp[i+1]+1)
        
        return sum(dp)
    
if __name__ == '__main__':
    
    solution = Solution()
#    print(solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
    print(solution.candy([1,0,2]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    