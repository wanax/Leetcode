'''
Xiaochi Ma
2018-11-25
'''
class Solution(object):
    
    def wordBreak2(self, s, wordDict):
        
        wordset = set(wordDict)
        dp = [False for i in range(len(s)+1)]      
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
        
        return dp[len(s)]
    
    def wordBreak3(self, s, wordDict):
         
         start = 0
         stack = [start]
         visited = set()

         while stack:
             start = stack.pop(0)
             if start in visited:
                 continue
             visited.add(start)
             for word in wordDict:
                 if s[start:].startswith(word):
                     count = len(word)
                     if len(s[start:]) == count:
                         return True
                     stack.append(start+count)
         
         return False
     
    def dfs1(self, s, wordDict, start, cur, res, visited):
        
        if start == len(s):
            res.append(" ".join(cur))
            return
        
        if start in visited:
            return
        
        for word in wordDict:
            if s[start:].startswith(word):
                cur.append(word)
                self.dfs(s, wordDict, start+len(word), cur, res, visited)
                cur.pop()
    
    def dfs(self, s, wordset, res, cache):
        if s in cache:
            return cache[s]
        if s == "":
            return [" "]
        ans = []
        i = 0
        while i < len(s):
            word = s[:i+1]
            if word in wordset:
                cur = self.dfs(s[i+1:], wordset, res, cache)
                for w in cur:
                    ans.append(word if w == " " else (word + ' ' + w))
            i += 1
        cache[s] = ans
        return ans
    
    def wordBreak(self, s, wordDict):
        
        res = []
        cache = {}
        wordset = set(wordDict)
        self.dfs(s, wordset, res, cache)
        return [ss.strip() for ss in cache[s]]
        
if __name__ == '__main__':
    
    solution = Solution()
    
#    print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
#    print(solution.wordBreak("leetcode", ["leet", "code"]))
#    print(solution.wordBreak("applepenapple", ["apple", "pen"]))
#    print(solution.wordBreak("cars", ["car","ca","rs"]))
#    print(solution.wordBreak("cbca", ["bc","ca"]))
#    print(solution.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
    
    
    print(solution.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"]))
    print(solution.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
    print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    




























