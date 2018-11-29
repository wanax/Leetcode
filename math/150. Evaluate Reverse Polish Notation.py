'''
Xiaochi Ma
2018-11-27
'''

class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for c in tokens:
            if self.isInt(c):
                stack.append(int(c))
            else:
                m = stack.pop()
                n = stack.pop()
                if c=="+":
                    stack.append(m+n)
                elif c=="-":
                    stack.append(n-m)
                elif c=="*":
                    stack.append(n*m)
                else:
                    stack.append(int(n/m))
        return stack[0]
    
    def isInt(self,num):
        try:
            num = int(str(num))
            return isinstance(num, int)
        except:
            return False
        
    def reverseWords(self, s):
        
        s = s.strip()
        ss = s.split(" ")
        ns = ""
        for word in ss[::-1]:
            if len(word) == 0:
                continue
            ns += word.strip() + " "
        
        return ns.strip()
    
    def maxProduct(self, nums):
        
        if len(nums) == 0:
            return 0
        
        res, low, high = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            oldH = high
            high = max(low*nums[i], high*nums[i], nums[i])
            low = min(low*nums[i], oldH*nums[i], nums[i])
            res = max(low, high, res)
        return res
    
    def findMin(self, nums):
        
        if len(nums) == 1:
            return nums[0]
        
        if nums[0] < nums[-1]:
            return nums[0]
        
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                while mid < r and nums[mid] <= nums[mid+1]:
                    mid += 1
                return nums[mid+1]
            elif nums[mid] < nums[r]:
                while mid > 0 and nums[mid] >= nums[mid-1]:
                    mid -= 1
                return nums[mid]
            else:
                r -= 1
        
        return nums[0]
    
if __name__ == '__main__':
    
    solution = Solution()
#    print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
#    print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
#    print(solution.evalRPN(["4", "13", "0", "/", "+"]))
#    print(solution.evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]))
    print(solution.findMin([10,1,10,10,10]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    