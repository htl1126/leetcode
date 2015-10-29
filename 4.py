# divide and conquer
# ref: https://leetcode.com/discuss/54023/python-o-log-min-m-n-solution

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        return self.FindKth(nums1, nums2, total_len / 2) if total_len % 2 == 1 else float(self.FindKth(nums1, nums2, total_len / 2 - 1) + self.FindKth(nums1, nums2, total_len / 2)) / 2

    def FindKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) / 2
        j = k - i
        if A[i] < B[j]:
            return self.FindKth(A[i:], B[:j], j)
        else:
            return self.FindKth(A[:i], B[j:], i)
