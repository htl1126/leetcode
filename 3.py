# ref: https://leetcode.com/discuss/64749/my-python
#      -solution-with-o-n-time-and-o-1-space
# keep track of last occurrence for each alphabet
# update longest sequence length when facing a new alphabet


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        str_len, max_len, begin, d = len(s), 1, 0, {s[0]: 0}
        for i in xrange(1, str_len):
            if s[i] in d and d[s[i]] >= begin:
                begin = d[s[i]] + 1
            max_len = max(max_len, i - begin + 1)
            d[s[i]] = i
        return max_len

if __name__ == '__main__':
    sol = Solution()
    print sol.lengthOfLongestSubstring('pwwkew')
