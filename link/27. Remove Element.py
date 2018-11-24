'''
Xiaochi Ma
2018-10-20
'''

MAX_INT = 2**31 - 1
MIN_INT = -2**31

class Solution:
    def removeElement(self, nums, val):
        
        while val in nums:
            nums.remove(val)
        return len(nums)
    
    def strStr(self, haystack, needle):
        
        if len(needle) == 0:
            return 0
        n = -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+(len(needle))] == needle:
                    n = i
                    break
        return n
    
    def divide(self, dividend, divisor):
        
        if divisor == 0 or (dividend == MIN_INT and divisor == -1) or (dividend == MAX_INT and divisor == 1):
            return MAX_INT
        
        if dividend == 0:
            return 0
        
        isPos = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        digits = 0
        while (divisor <= dividend):
            divisor <<= 1
            digits += 1
        
        divisor >>= digits
        digits -= 1
        
        result = 0
        while digits >= 0:
            if dividend >= (divisor << digits):
                dividend -= divisor << digits
                result += (1 << digits)
            digits -= 1
        
        return result if isPos else -result


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.divide(7, -3))
























