'''
Xiaochi Ma
2018-11-15
'''

class Solution:
    
    def fullJustify(self, words, maxWidth):
        
        res = []
        index = 0
        while index < len(words):
            count = len(words[index])
            last = index + 1
            while last < len(words):
                if count + 1 + len(words[last]) > maxWidth:
                    break
                count += 1 + len(words[last])
                last += 1
            strs = ""
            strs += words[index]
            diff = last - index - 1
            if last == len(words) or diff == 0:
                for i in range(index+1, last):
                    strs += " "
                    strs += words[i]
                for i in range(len(strs), maxWidth):
                    strs += " "
            else:
                spaces = (maxWidth - count) // diff
                r = (maxWidth - count) % diff
                for i in range(index+1, last):
                    for k in range(0, spaces):
                        strs += " "
                    if r > 0:
                        strs += " "
                        r -= 1
                    strs += " "
                    strs += words[i]
            res.append(strs)
            index = last
                
        return res
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    