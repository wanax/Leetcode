'''
Xiaochi Ma
2018-12-04
'''

class Solution:

    def reverseBits(self, n):
        
        s = "{:032b}".format(n)
        
        return s.count('1')
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.reverseBits(43261596))