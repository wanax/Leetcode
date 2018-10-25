'''
Xiaochi Ma
2018-10-16
'''

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left <= right:
            area = (right - left) * min(height[left], height[right])
            if area > maxArea:
                maxArea = area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return maxArea
        
        

if __name__ == '__main__':
    
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))








































