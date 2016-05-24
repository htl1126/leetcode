import bisect


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums2.sort()
        ans = []
        for num in nums1:
            idx = bisect.bisect_left(nums2, num)
            if 0 <= idx < len(nums2) and nums2[idx] == num:
                ans.append(num)
                del nums2[idx]
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.intersect([1, 2], [1, 1])
