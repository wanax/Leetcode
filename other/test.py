'''
Xiaochi Ma
2019-01-22
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.vis = False

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         
import string
import math
import heapq
import collections
import sys
import bisect
from functools import reduce
import re
import string

class Node:
    def __init__(self, val):
        self.val = val
        self.next = 0
        self.random = 0
        
class Solution(object):
    
    def dfs(self, n, i, j, mem):
        if n == 0:
            return 1
        if (i,j,n) in mem:
            return mem[(i,j,n)]
        cur = 0
        vs = [[1,-2],[1,2],[-1,-2],[-1,2],[2,-1],[2,1],[-2,-1],[-2,1]]
        for v in vs:
            ni, nj = i+v[0], j+v[1]
            if (0<=ni<=2 and 0<=nj<=2) or (ni==3 and nj==1):
                cur += self.dfs(n-1, ni, nj, mem)%(10**9+7)
        mem[(i,j,n)] = cur
        return cur
    def knightDialer(self, N):
        mem = {}
        ans = 0
        for i in range(3):
            for j in range(3):
                ans += self.dfs(N-1, i, j, mem)
        ans += self.dfs(N-1, 3, 1, mem)
        return ans%(10**9+7)
                
    
if __name__ == '__main__':
    
    so = Solution()
    print(so.knightDialer(3589))





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
