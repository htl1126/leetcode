# Ref: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/discuss/472027/Python3-faster-over98

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        def search(x):
            l, r = 0, len(arr)
            while l < r:
                m = (l + r) // 2
                if arr[m] < x:
                    l = m + 1
                else:
                    r = m
            return l
        
        for i in range(1, 4):
            idx = int(i * len(arr) / 4)
            start = search(arr[idx])
            if arr[start] == arr[start + len(arr) // 4]:
                return arr[start]
