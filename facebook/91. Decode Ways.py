'''
Xiaochi Ma
2018-11-02
'''

class Solution:
    
    def back(self, strs, res, cur):
        
        if len(strs) == 0:
            res.append(cur[:])
        
        if len(strs) > 0:
            num = strs.pop(0)
            if int(num) > 0:
                c = chr(int(num)-1 + ord('A'))
                cur.append(c)
                self.back(strs[:], res, cur)
                cur.pop(0)
                strs.insert(0, num)
            else:
                return
            
        if len(strs) > 1:
            num1 = strs.pop(0)
            num2 = strs.pop(0)
            if int(num1+num2) < 27:
                c = chr(int(num1+num2) - 1 + ord('A'))
                cur.append(c)
                self.back(strs[:], res, cur)
                cur.pop(0)
                strs.insert(0, num2)
                strs.insert(0, num1)
            else:
                return
    
    def numDecodings1(self, s):
        
        if len(s) == 0:
            return 0
        
        res = []
        self.back(list(s), res, [])
        
        return len(res)
    
    def numDecodings(self, s):
        
        dp = [0 for i in range(len(s)+1)]
        
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] < '27' and s[i-2:i] > '09':
                dp[i] += dp[i-2]
        
        return dp[len(s)]
    
    
if __name__ == '__main__':
    
    
    solution = Solution()
    print(solution.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"))   
#    print(solution.numDecodings("112"))   






























