'''
Xiaochi Ma
2018-11-01
'''

class Solution:
    
    def leastInterval(self, tasks, n):
        
        chars = [0 for i in range(26)]
        for c in tasks:
            chars[ord(c)-ord('A')] += 1
            
        chars.sort()
        
        time = 0
        step = 0
        while chars[-1] > 0:
            chars[-1] -= 1
            time += 1
            for i in range(len(chars)-2, -1, -1):
                if step == n or sum(chars) == 0:
                    break
                if chars[i] > 0:
                    chars[i] -= 1
                time += 1
                step += 1
            if sum(chars) != 0:
                time += (n - step)
            chars.sort()
            step = 0
        return time
    
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.leastInterval(["A","A","A","B","B","B"], 50))

    






















