'''
Xiaochi Ma
2018-11-08
'''

class Solution:
    
    def isPali(self, word):
        return word == word[::-1]
    
    def palindromePairs(self, words):
        
        dic = {}
        for i in range(len(words)):
            dic[words[i]] = i
        
        res = []
        
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                rest = word[:j]
                reverse = word[j:][::-1]
                if self.isPali(rest) and (reverse in dic) and (dic[reverse] != i):
                    res.append([dic[reverse], i])
                
                if j == len(word): continue
                    
                rest = word[j:]
                reverse = word[:j][::-1]
                if self.isPali(rest) and (reverse in dic) and (dic[reverse] != i):
                    res.append([i, dic[reverse]])
        
        return res
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.palindromePairs(["abcd","dcba","lls","s","sssll"]))
    
    
    
    
    
    
    
    
    
    
    
    