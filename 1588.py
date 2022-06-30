# Ref: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/discuss/854184/JavaC%2B%2BPython-O(N)-Time-O(1)-Space

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans, n = 0, len(arr)
        for i, v in enumerate(arr):
            ans += ((i + 1) * (n - i) + 1) // 2 * v
        return ans
