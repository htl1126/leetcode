# Ref: https://leetcode.com/problems/two-sum-less-than-k/discuss/323522/Python-simple-solution

class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i, j, ans = 0, len(A) - 1, -1
        a = sorted(A)
        while i < j:
            if a[i] + a[j] < K:
                ans = max(ans, a[i] + a[j])
                i += 1
            else:
                j -= 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 60)
