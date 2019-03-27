'''
Xiaochi Ma
2018-10-17
'''
from itertools import product

class Solution:
    def letterCombinations(self, digits):
        
        if len(digits) == 0:
            return []
        
        vals = {'2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'}
        res_set = []
        
        
        for i in digits:
            res_set.append(vals[i])
            
        C = []
        for i in product(*res_set):
                C.append("".join(i))
        return C
        
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.letterCombinations(''))




















