'''
Xiaochi Ma
2018-11-17
'''

class Solution:
    
    def largestRectangleArea(self, heights):
        
        if len(heights) == 0:
            return 0
        
        res = 0
        stack = []
        
        for i in range(len(heights)+1):
            h = 0
            if i == len(heights):
                h = 0
            else:
                h = heights[i]
            
            while len(stack) > 0 and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                start = -1 if len(stack) == 0 else stack[-1]
                area = height * (i - start - 1)
                res = max(res, area)
            stack.append(i)
        
        return res
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.largestRectangleArea([1,2,3,4,5])) 
