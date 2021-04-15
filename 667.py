# Ref: https://leetcode.com/problems/beautiful-arrangement-ii/discuss/106965/Python-Straightforward-with-Explanation

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = list(range(1, n - k))
        for d in range(k + 1):
            if d % 2 == 0:
                ans.append(n - k + d // 2)
            else:
                ans.append(n - d // 2)
        return ans
