# Ref: https://leetcode.com/problems/find-smallest-common-element-in-all-rows/discuss/387092/JavaC%2B%2BPython-Brute-Force-Count
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        c = collections.Counter()
        for row in mat:
            for i in row:
                c[i] += 1
                if c[i] == len(mat):
                    return i
        return -1
