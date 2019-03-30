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
import numpy as np

class Node:
    def __init__(self, val):
        self.val = val
        self.next = 0
        self.random = 0
        
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        pres = [0]*numCourses
        dic = collections.defaultdict(list)
        for pre in prerequisites:
            pres[pre[0]] += 1
            dic[pre[1]].append(pre[0])
        q = []   
        for i, c in enumerate(pres):
            if c == 0:
                q.append(i)
        
        vis = q[:]
        while q:
            k = len(q)
            for i in range(k):
                p = q.pop(0)
                for c in dic[p]:
                    pres[c] -= 1
                    if pres[c] == 0:
                        q.append(c)
                        vis.append(c)
        return vis
    
if __name__ == '__main__':
    
    so = Solution()
    print(so.findOrder(2, [[1,0]]))
    arr = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    arr.sort(key=lambda x: (x[1],x[0]))
    print(arr)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
