'''
Xiaochi Ma
2018-12-06
'''

class Solution(object):
    
    def countPrimes(self, n):
        
        n = n-1
        m = [True for i in range(n+1)]    
        p = 2
        while p * p <= n:
            if m[p]:
                for i in range(p*p, n+1, p):
                    m[i] = False
            p += 1
        
        return m[2:].count(True)
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.countPrimes(2))