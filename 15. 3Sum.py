'''
Xiaochi Ma
2018-10-17
'''

class Solution(object):
    def threeSum(self, nums):
        
        nums.sort()
        
        N, results = len(nums), []
        for i in range(N):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = nums[i] * -1
            s, e = i + 1, N - 1
            while s < e:
                if nums[s] + nums[e] == target:
                    results.append([nums[i], nums[s], nums[e]])
                    s += 1
                    while s < e and nums[s-1] == nums[s]:
                        s += 1
                elif nums[s] + nums[e] < target:
                    s += 1
                else:
                    e -= 1
        return results

if __name__ == '__main__':
    
    arr = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print(solution.threeSum(arr))
        
        
    














