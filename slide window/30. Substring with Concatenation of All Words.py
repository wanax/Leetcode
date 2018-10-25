'''
Xiaochi Ma
2018-10-21
'''

import collections

class Solution:
    def findSubstring(self, s, words):
        
        if len(words) == 0:
            return []
        
        counter = collections.Counter(words)
        x = len(words[0])
        result = []
        
        for n in range(x):
            dic = {}
            count = 0
            head = n
            for i in range(n, len(s) - x + 1, x):
                
                temp = s[i:i+x]
                if temp in counter:
                    
                    dic[temp] = dic.get(temp, 0) + 1
                    count += 1
                
                    while dic[temp] > counter[temp]:
                        dic[s[head:head+x]] -= 1
                        count -= 1
                        head += x
                    if count == len(words):
                        result.append(head)
                else:
                    head = i + x
                    dic = {}
                    count = 0
        
        return result
        
        
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.findSubstring('foobarfoobar', ["foo","bar"]))

































