'''
Xiaochi Ma
2018-11-10
'''

class Solution:
    
    def wordsTyping(self, sentence, rows, cols):
        
        s = ""
        for word in sentence:
            s += word
            s += " "
            
        count = 0
        n = len(s)
        for i in range(rows):
            count += cols
            if s[count%n] == " ":
                count += 1
            else:
                while count > 0 and s[(count-1)%n] != " ":
                    count -= 1
        
        return count // n
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.wordsTyping(["f","p","a"], 8, 7))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    