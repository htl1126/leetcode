# ref: https://discuss.leetcode.com/topic/7399/share-my-c-solution
import collections


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        j, d, maxlen, count = -1, collections.defaultdict(int), 0, 0
        for i in xrange(len(s)):
            d[s[i]] += 1
            if d[s[i]] == 1:
                count += 1
            while count > 2:
                j += 1
                d[s[j]] -= 1
                if not d[s[j]]:
                    del d[s[j]]
                    count -= 1
            maxlen = max(maxlen, i - j)
        return maxlen

if __name__ == '__main__':
    sol = Solution()
    print sol.lengthOfLongestSubstringTwoDistinct('abc')
