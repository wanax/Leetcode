'''
Xiaochi Ma
2018-12-06
'''

class Solution(object):
    
    def isIsomorphic(self, s, t):
        
        if len(s) != len(t):
            return False
        
        dic = {}
        dic2 = {}
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in dic2:
                    return False
                dic[s[i]] = t[i]
                dic2[t[i]] = s[i]
            else:
                if dic[s[i]] != t[i]:
                    return False
        return True
    
if __name__ == '__main__':
    
    solution = Solution()
#    print(solution.isIsomorphic("egg", "add"))
#    print(solution.isIsomorphic("foo", "bar"))
#    print(solution.isIsomorphic("paper", "title"))
    print(solution.isIsomorphic("ab", "aa"))
