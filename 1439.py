# Ref: https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/discuss/609678/Python-O(k-*-logk-*-len(mat))-with-detailed-explanations-%2B-4-lines-python.
# Ref: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84550/Slow-1-liner-to-Fast-solutions

class Solution:
    def kthSmallestPairs(self, nums1, nums2, k):
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, (nums1[i] + nums2[j], i, j))
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append(nums1[i] + nums2[j])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs
    
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        res = mat[0]
        for i in range(1, m):
            res = self.kthSmallestPairs(res, mat[i], k)
        return res[k - 1]
