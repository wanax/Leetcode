'''
Xiaochi Ma
2019-01-22
'''
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
#        self.vis = False
#
#class Interval:
#    def __init__(self, s=0, e=0):
#        self.start = s
#        self.end = e
#        
#class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#         
#class Node(object):
#    def __init__(self, val, next, random):
#        self.val = val
#        self.next = next
#        self.random = random

#import random
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
from functools import reduce
from decimal import *
from decimal import Decimal
import decimal
from statistics import mode
import datetime
import itertools
from functools import lru_cache

heap = []
def heapSort(arr):
    for i in range(len(arr)):
        heap.append(arr[i])
        switch(heap, len(heap)-1)
    ans = []
    while heap:
        ans.append(heap.pop(0))
        switch(heap, len(heap)-1)
    return ans[::-1]
        
def switch(heap, i):
    if i <= 0:
        return
    par = (i-1)//2
    old_par = heap[par]
    l, r = 2*par+1, 2*par+2
    t, idx = heap[par], par
    if l < len(heap) and heap[l] > t:
        t, idx = heap[l], l
    if r < len(heap) and heap[r] > t:
        t, idx = heap[r], r
    heap[par], heap[idx] = heap[idx], heap[par]
    if heap[par] != old_par:
        switch(heap, par)
    
#arr = [2,5,8,9,6,3,7,4,5]
#print(heapSort(arr)) 
    
    
def compress(x1, x2, w):
    xs = []
    for i in range(len(x1)):
        for d in range(-1, 2):
            tx1, tx2 = x1[i]+d, x2[i]+d
            if 1<=tx1 and tx1<=w:
                xs.append(tx1)
            if 1<=tx2 and tx2<=w:
                xs.append(tx2)
        
    xs.sort()
    print(xs)
    for n in set(xs):
        xs.remove(n)
    return xs

x1 = [1, 1, 4, 9, 10]
x2 = [6, 10, 4, 9, 10]

print(compress(x1, x2, 10))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
