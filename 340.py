# ref: https://discuss.leetcode.com/topic/41711/8-lines-c-o-n-8ms/4
import collections


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        j, maxlen, ctr = -1, 0, collections.Counter()
        for i, c in enumerate(s):
            ctr[c] += 1
            while len(ctr) > k:
                j += 1
                ctr[s[j]] -= 1
                if ctr[s[j]] == 0:
                    del ctr[s[j]]
            maxlen = max(maxlen, i - j)
        return maxlen

if __name__ == '__main__':
    sol = Solution()
    print sol.lengthOfLongestSubstringKDistinct('eceba', 2)
