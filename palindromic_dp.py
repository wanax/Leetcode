'''
Xiaochi Ma
2018-10-06
'''

class Solution(object):
    def longestPalindrome(self, s):
        string = s
        martix = [[0 for i in range(len(string))] for j in range(len(string))]
    
        if len(string) == 0:
            print("")
        if len(string) == 1:
            print(string)
            
        for i in range(len(string)):
            for j in range(len(string)):
                if i >= j:
                    martix[i][j] = 1
            
        step = 1
        maxLen = 1
        left = 0
        right = 0
        for step in range(1, len(string)):
           for i in range(len(string) - step):
               j = i + step
               if string[i] != string[j]:
                   martix[i][j] = 0
               else:
                   martix[i][j] = martix[i+1][j-1]
                   if martix[i][j] == 1:
                       if step + 1 > maxLen:
                           maxLen = step + 1
                           left = i
                           right = j
        return string[left:right+1]
        

if __name__ == '__main__':
    
#    solution = Solution()
#    print(solution.longestPalindrome("cbbd"))            

    string = 'cbbd'
    martix = [[0 for i in range(len(string))] for j in range(len(string))]

    if len(string) == 0:
        print("")
    if len(string) == 1:
        print(string)
        
    for i in range(len(string)):
        for j in range(len(string)):
            if i >= j:
                martix[i][j] = 1
        
    step = 1
    maxLen = 1
    left = 0
    right = 0
    for step in range(1, len(string)):
       for i in range(len(string) - step):
           j = i + step
           if string[i] != string[j]:
               martix[i][j] = 0
           else:
               martix[i][j] = martix[i+1][j-1]
               if martix[i][j] == 1:
                   if step + 1 > maxLen:
                       maxLen = step + 1
                       left = i
                       right = j
    print(string[left:right+1]) 

































