'''
Xiaochi Ma
2018-10-26
'''
class Solution:
    
    def trap(self, height):
    
        area = 0
        visited = []
        for i in range(len(height)):
            if height[i] == 0 or i in visited:
                continue
            for j in range(i+1, len(height)):
                if height[j] >= height[i]:
                    h = height[i]
                    w = j - i - 1
                    area += h * w - (sum([height[x] for x in range(i+1, j)]))
                    for x in range(i+1, j):
                        visited.append(x)
                    break
                
        return area


if __name__ == '__main__':
    
#    solution = Solution()
#    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))


    dp = [[False] * 3 for _ in range(5)]
    print(dp)





















