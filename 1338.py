# Ref: https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/1319416/C%2B%2BJavaPython-HashMap-and-Sort-then-Counting-Sort-O(N)-Clean-and-Concise

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # remove numbers of high frequencies first until remaining set size less than half

        n, c = len(arr), collections.Counter(arr)
        count = [0] * (n + 1)
        for f in c.values():
            count[f] += 1
        ans, removed, half, freq = 0, 0, n // 2, n
        while removed < half:
            ans += 1
            while count[freq] == 0:
                freq -= 1
            removed += freq
            count[freq] -= 1
        return ans
