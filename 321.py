# ref: https://discuss.leetcode.com/topic/32298/short-python-ruby-c


class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def prep(nums, k):  # take k largest numbers and preserve the order
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(a, b):  # merge two sequences and preserve the order
            return [max(a, b).pop(0) for _ in a + b]
        return max(merge(prep(nums1, i), prep(nums2, k - i))
                   for i in xrange(k + 1)
                   if i <= len(nums1) and k - i <= len(nums2))

if __name__ == '__main__':
    sol = Solution()
    print sol.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
