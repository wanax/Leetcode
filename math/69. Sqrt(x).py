'''
Xiaochi Ma
2018-11-15
'''

class Solution:
    
    def mySqrt(self, x):
        
        l, r = 1, x
        while l <= r:
            mid = (l + r)//2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                r = mid - 1
            else:
                l = mid + 1
        
        return l-1
    
    def climbStairs(self, n):
        
        dp = [0 for i in range(max(3, n+1))]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        if n < 3:
            return dp[n]
        
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] 
        
        return dp[n]
    
    def simplifyPath(self, path):
        
        paths = path.split('/')
        stack = []
        for op in paths:
            if op == '..':
                if len(stack) > 0:
                    stack.pop()
            elif op != '' and op != '.':
                stack.append(op)
                
        res = ""
        for op in stack:
            res += "/" + op
        
        return res if len(res) > 0 else "/"
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.simplifyPath("/")) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    