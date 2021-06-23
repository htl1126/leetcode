# Ref: https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)

# x - A[mid] > A[mid + k] - x => (A[mid] + A[mid + k]) / 2 < x => choose A[mid + 1] ... A[mid + k]
#                      otherwise (A[mid] + A[mid + k]) / 2 >= x => choose A[mid] ... A[mid + k - 1]
# [1, 2, 3, 4, 5], k = 4, x = 3, choose [1, 2, 3, 4] over [2, 3, 4, 5] since [1, 2, 3, 4]'s lexicographical order is lower.

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) // 2
            if (arr[m] + arr[m + k]) // 2 < x:
                l = m + 1
            else:
                r = m
        return arr[l:l + k]

if __name__ == "__main__":
    sol = Solution()
    print sol.findClosestElements([1, 2, 3, 4, 5], 4, 3)
