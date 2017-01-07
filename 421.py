# https://discuss.leetcode.com/topic/63299/python-6-lines-bit-by-bit


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            # if (answer^1 ^ p) and p are both in the prefixes set, then we
            # can keep answer^1 because (answer^1 ^ p) ^ p == answer^1
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
        return answer

if __name__ == '__main__':
    sol = Solution()
    print sol.findMaximumXOR([3, 10, 5, 25, 2, 8])
