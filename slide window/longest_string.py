#######################

# Machine Learning Test 2018/10/01
# Miles Ma
#
########################

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        wordSet = set()
        maxCount = 0
        i,j = 0,0
        for i in range(len(s)):
            while j < len(s) and s[j] not in wordSet:
                wordSet.add(s[j])
                j += 1
                maxCount = max(maxCount, j - i)
            wordSet.remove(s[i])
        return maxCount


if __name__ == "__main__":
    
    string = 'abcabcbb'
    solution = Solution()
    print(solution.lengthOfLongestSubstring(string))









































