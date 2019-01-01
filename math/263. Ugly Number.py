'''
Xiaochi Ma
2018-12-17
'''
import heapq
class Solution(object):
    
    def isUgly(self, num):
        
        if num == 0:
            return False
        
        fs = [5, 3, 2]
        for f in fs:
            while num%f == 0:
                num = num/f
        
        return True if num == 1 else False
    
    def nthUglyNumber2(self, n):
        
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        heap = [2, 3, 5]
        heapq.heapify(heap)
        
        for i in range(1, n):
            item = heapq.heappop(heap)
            if item*2 not in heap:
                heapq.heappush(heap, item*2)
            if item*3 not in heap:
                heapq.heappush(heap, item*3)
            if item*5 not in heap:
                heapq.heappush(heap, item*5)
        
        return item
    
    def nthUglyNumber(self, n):

        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min(u2, u3, u5)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]
    
    def nthSuperUglyNumber(self, n, primes):
        
        res = [1]
        ii = [0] * len(primes)
        while len(res) < n:
            los = list(map(lambda x,y:x*res[y], primes, ii))
            um = min(los)
            for i in range(len(primes)):
                if los[i] == um:
                    ii[i] += 1
#            if um not in res:
            res.append(um)
        
        return res[-1]
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.nthSuperUglyNumber(12, [2,7,13,19]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    