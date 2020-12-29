# Ref: https://leetcode.com/problems/smallest-range-ii/discuss/173377/C%2B%2BJavaPython-Add-0-or-2-*-K

class Solution:
    def smallestRangeII(self, A: list, K: int) -> int:
        A.sort()
        ans = A[-1] - A[0]
        for i in range(len(A) - 1):
            big = max(A[i] + 2 * K, A[-1])
            small = min(A[0] + 2 * K, A[i + 1])
            ans = min(big - small, ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestRangeII([1, 3, 6], 3))
