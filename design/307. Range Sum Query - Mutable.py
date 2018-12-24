'''
Xiaochi Ma
2018-12-24
'''

class SegmentTreeNode:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.sum = 0
        self.left = None
        self.right = None

class NumArray:
    
    def _build_segment_tree(self, array, start, end):
        if start > end:
            return None
        cur = SegmentTreeNode(start, end)
        if start == end:
            cur.sum = array[start]
            return cur
        mid = start + (end-start)//2
        cur.left = self._build_segment_tree(array, start, mid)
        cur.right = self._build_segment_tree(array, mid+1, end)
        if cur.left is not None:
            cur.sum += cur.left.sum
        if cur.right is not None:
            cur.sum += cur.right.sum
        return cur
    
    def _get_sum_from_tree(self, cur, start, end):
        if not cur or cur.s > end or cur.e < start:
            return 0
        if cur.s >= start and cur.e <= end:
            return cur.sum
        return self._get_sum_from_tree(cur.left, start, end) + self._get_sum_from_tree(cur.right, start, end)

    def __init__(self, nums):
        self.array = nums
        self.root = self._build_segment_tree(nums, 0, len(nums)-1)
        

    def update(self, i, val):
        diff = val - self.array[i]
        self.array[i] = val
        cur = self.root
        while cur:
            cur.sum += diff
            mid = cur.s + (cur.e-cur.s)//2
            if i <= mid:
                cur = cur.left
            else:
                cur = cur.right
        

    def sumRange(self, i, j):
        return self._get_sum_from_tree(self.root, i, j)
        
obj = NumArray([0,9,5,7,3])
obj.update(1,2)
print(obj.sumRange(0,2))




























