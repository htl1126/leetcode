import heapq
# ref: https://discuss.leetcode.com/topic/50450/slow-1-liner-to-fast-solutions


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        queue, pairs = [], []

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:  # avoid duplicate pairs
                push(i + 1, j)
        return pairs

if __name__ == '__main__':
    sol = Solution()
    print sol.kSmallestPairs([1, 7, 11], [2, 4, 6], 3)
