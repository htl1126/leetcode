# Ref: https://leetcode.com/problems/3sum-with-multiplicity/discuss/181131/C%2B%2BJavaPython-O(N-%2B-101-*-101)

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        cnt = collections.Counter(arr)
        nums = list(cnt.keys())
        ans = 0
        for a in range(len(nums)):
            for b in range(a, len(nums)):
                i, j = nums[a], nums[b]
                k = target - i - j
                if i == j == k:
                    ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
                elif i == j != k:
                    ans += cnt[i] * (cnt[i] - 1) // 2 * cnt[k]
                elif i < k and j < k:
                    ans += cnt[i] * cnt[j] * cnt[k]
        return ans % (10 ** 9 + 7)
