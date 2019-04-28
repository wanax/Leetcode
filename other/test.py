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
    def rearrangeString(self, s, k):
        count = collections.Counter(s)
        order = collections.OrderedDict(sorted(count.items(), key=lambda x:x[1], reverse=True))
        
        keys = list(order.keys())
        bucks = [[keys[0]] for i in range(order[keys[0]])]
        
        i = 1
        row = 0
        while i < len(keys):
            c = order[keys[i]]
            while c > 0:
                bucks[row].append(keys[i])
                row = (row+1)%(len(bucks)-1)
                c -= 1
            i += 1
            
        for i, row in enumerate(bucks):
            if i != len(bucks)-1:
                if len(row) < k:
                    return ""
        
        return "".join(list(reduce(lambda x,y:x+y, bucks)))
    
if __name__ == '__main__':
    
    s = Solution()
    print(s.rearrangeString("abeabac", 3))
    
    print(1%3)
        
    
    


    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
