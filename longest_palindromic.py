#######################

# Machine Learning Test 2018/10/06
# Miles Ma
#
########################

class Solution(object):
    def longestPalindrome(self, s):
        
        arr = s
        newArr = ""
        for i in range(len(arr)):
            newArr += '#'
            newArr += arr[i]
        newArr += '#'
            
        p = [0 for x in range(0, len(newArr))]
        c = 0
        r = 0
        for i in range(1, len(newArr) - 1):
            i_mirror = c - (i - c)
            if i >= r:
                p[i] = 0
            elif i + p[i_mirror] < r:
                p[i] = p[i_mirror]
            else:
                p[i] = r - i
            
            while (i + p[i] + 1 < len(newArr) and newArr[i + p[i] + 1] == newArr[i - p[i] - 1]):
                p[i] += 1
            
            if i + p[i] > r:
                c = i
                r = i + p[i]
                
        maxLen = 0
        cIndex = 0
        for i in range(1, len(newArr) - 1):
            if p[i] > maxLen:
                maxLen = p[i]
                cIndex = i
        
        return newArr[cIndex - p[cIndex]:p[cIndex] + cIndex + 1].replace('#','')

if __name__ == '__main__':
    
    string = 'aba'
    solution = Solution()
    print(solution.longestPalindrome(string))






























