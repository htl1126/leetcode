# Ref: https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = count = 0
        d = {0: 0}
        for i, num in enumerate(nums, 1):
            count += 1 if num else -1
            max_len = max(max_len, i - d.setdefault(count, i))
        return max_len

if __name__ == "__main__":
    sol = Solution()
    print sol.findMaxLength([0, 1, 0])
