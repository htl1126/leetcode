# Ref: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/256729/JavaC%2B%2BPython-Binary-Search
# Algo: binary search

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left, right = max(weights), sum(weights)
        while left < right:
            mid, need, cur = (left + right) / 2, 1, 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == "__main__":
    sol = Solution()
    print sol.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
