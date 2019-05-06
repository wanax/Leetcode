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

import random
import functools
import copy
from operator import itemgetter         
import string
import math
import heapq
import collections
import sys
import bisect
from functools import reduce
import re
import string
import numpy as np
from itertools import permutations 

class Solution(object):
    def dfs(self, s, p, i, j, mem):
        if j == len(p):
            if i == len(s):
                return True
            else:
                return False
        if (i, j) in mem > 0:
            return mem[i,j]
        tag = False
        first_m = (i<len(s) and (s[i] == p[j] or p[j]=='.'))
        if j+1<len(p) and p[j+1]=='*':
            tag = (first_m and self.dfs(s, p, i+1, j, mem)) or self.dfs(s, p, i, j+2, mem)
        else:
            tag = first_m and self.dfs(s, p, i+1, j+1, mem)
            
        if tag:
            mem[i, j] = True
        return tag
                
    def isMatch(self, s, p):
        mem = {}
        return self.dfs(s, p, 0, 0, mem)
                    
                    
    
if __name__ == '__main__':
    
    s = Solution()
    print(s.isMatch("ab",".*"))
    
    
    
    


    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
