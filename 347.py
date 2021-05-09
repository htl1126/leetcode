# ref: https://leetcode.com/problems/top-k-frequent-elements/discuss/740374/Python-5-lines-O(n)-buckets-solution-explained.
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]  # for freq 0 to n
        count = collections.Counter(nums)
        for n, f in count.items():
            bucket[f].append(n)
        res = list(chain(*bucket))
        return res[::-1][:k]

if __name__ == '__main__':
    sol = Solution()
    print sol.topKFrequent([1, 1, 2, 2, 2, 3], 2)
