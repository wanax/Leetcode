'''
Xiaochi Ma
2018-12-12
'''
import collections
class Solution(object):
    
    def shortestWordDistance(self, words, word1, word2):
        
        self.dic = collections.defaultdict(list)
        self.length = len(words)
        for i in range(len(words)):
            arr = self.dic.get(words[i], [])
            arr.append(i)
            self.dic[words[i]] = arr
            
        idx1 = self.dic[word1]
        idx2 = self.dic[word2]

        res = 2**32
        i, j = 0, 0
        while i < len(idx1) and j < len(idx2):
            if idx1[i] == idx2[j]:
                i += 1
                continue
            res = min(abs(idx1[i]-idx2[j]), res)
            if idx1[i] < idx2[j]:
                i += 1
            else:
                j += 1
        
        return res

if __name__ == '__main__':
    
    solution = Solution()
    print(solution.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes","makes"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    