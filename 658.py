# Ref: https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)

# arr[m], arr[m + 1], ..., arr[m + k - 1]
#         arr[m + 1], ..., arr[m + k - 1], arr[m + k]
# We want to know, for arr[m] and arr[m + k], which one is closer to x.
# If x < arr[m], the window will keep moving left.
# If x > arr[m + k], the window will keep moving right.
# [1, 2, 3, 4, 5], k = 4, x = 3, choose [1, 2, 3, 4] over [2, 3, 4, 5] since [1, 2, 3, 4]'s lexicographical order is lower.

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l + k]

if __name__ == "__main__":
    sol = Solution()
    print sol.findClosestElements([1, 2, 3, 4, 5], 4, 3)
