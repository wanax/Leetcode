'''
Xiaochi Ma
2018-11-17
'''

class Solution:

    def maximalRectangle(self, matrix):
        
        if len(matrix) == 0:
            return 0
        
        ncol = len(matrix[0])
        heights = [0 for i in range(ncol+1)]
        heights[ncol] = 0
        res = 0
        
        for row in range(len(matrix)):
            stack = []
            for i in range(ncol+1):
                if i < ncol:
                    if matrix[row][i] == '1':
                        heights[i] += 1
                    else:
                        heights[i] = 0
                if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                    stack.append(i)
                else:
                    while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                        cur = heights[stack.pop()] * (i if len(stack) == 0 else (i - stack[-1] - 1))
                        res = max(res, cur)
                    stack.append(i)
        
        return res
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.maximalRectangle([
                                      ["1","0","1","0","0"],
                                      ["1","0","1","1","1"],
                                      ["1","1","1","1","1"],
                                      ["1","0","0","1","0"]
                                    ])) 






















