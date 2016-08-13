# ref: https://discuss.leetcode.com/topic/46685/python-solution-beats-99-67


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for w in words:
            mask = 0
            for c in w:
                mask |= 1 << (ord(c) - ord('a'))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])

if __name__ == '__main__':
    sol = Solution()
    print sol.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
