'''
Xiaochi Ma
2018-11-01
'''


class Solution:
    
    def findAnagrams(self, s, p):
        
        index = []
        cset = set(list(p))
        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(cset) == 0:
                    index.append(j-len(p))
                    cset = set(list(p))
                if s[j] in cset:
                    cset.remove(s[j])
                else:
                    cset = set(list(p))
                    continue
        
        return index
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.findAnagrams("abab", "ab"))