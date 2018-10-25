'''
Xiaochi Ma
2018-10-16
'''

class Solution1(object):
    def intToRoman(self, num):
        res = ""
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        digit = 0
        while num > 0:
            times = int(num / nums[digit])
            num -= times * nums[digit]
            for i in range(times, 0, -1):
                res += symbols[digit]
            digit += 1
        return res
    
class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]
        

if __name__ == '__main__':
    
    solution = Solution()
    print(solution.longestCommonPrefix(["aa","a"]))
























