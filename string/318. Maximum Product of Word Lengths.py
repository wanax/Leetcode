'''
Xiaochi Ma
2018-12-27
'''

class Solution:
    
    def maxProduct(self, words):
        
        bins = []
        for word in words:
            b = 0
            for c in word:
                b |= (1<<(ord(c)-ord('a')))
            bins.append(b)
            
        t = 0
        for i in range(len(bins)-1):
            for j in range(1, len(bins)):
                if bins[i]&bins[j] == 0:
                    t = max(t, len(words[i])*len(words[j]))
        return t
    
    def removeDuplicateLetters(self, s):
        
        b = 0
        for c in s:
            b |= (1<<(ord(c)-ord('a')))
            
        n = ""
        while b > 0:
            i = b&(-b)
            ss = "{0:b}".format(i)
            n += chr((len(ss)-1+ord('a')))
            b -= i
            
        dic = set(n)
        res = []
        for c in s:
            if c in dic and c not in res:
                res.append(c)
        
        return n
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.removeDuplicateLetters("cbacdcbc"))
    
    
                    
        
#    t = 1
#    t2 = 1<<1
#    t3 = 1<<1
#    
#    t4 = 1<<2
#    t5 = 1<<4
#    t6 = 1<<5
#
#    print(t|t2|t3)
#    print(t4|t5|t6)
#    
#    a = t|t2|t3
#    b = t4|t5|t6
#    
#    print(bin(a))
#    print(bin(b))
#    
#    print(a&b)
    
    
    
    
    
    
    
    
    
    
    
    
    
    