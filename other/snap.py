# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 23:11:16 2021

@author: mxiao
"""

class SnapshotArray(object):

    def __init__(self, length):
        self.arr = [0 for _ in range(length)]
        self.change = [{} for _ in range(length)]
        self.snap = 0

    def set(self, index, val):
        self.change[index][self.snap] = val
        self.arr[index] = val
        

    def snap(self):
        self.snap += 1
        return self.snap-1
        

    def get(self, index, snap_id):
        dic = self.change[index]
        if snap_id in dic:
            return dic[snap_id]
        return 0
    
obj = SnapshotArray(5)
obj.set(0, 5)
obj.snap()