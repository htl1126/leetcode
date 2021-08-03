# ref: https://leetcode.com/problems/total-hamming-distance/discuss/96228/Python-Explanation


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bits = [[0, 0] for _ in range(32)]
        for n in nums:
            for bit in bits:
                bit[n % 2] += 1
                n >>= 1
        return sum(i * j for i, j in bits)

if __name__ == '__main__':
    sol = Solution()
    print sol.totalHammingDistance([4, 14, 2])
