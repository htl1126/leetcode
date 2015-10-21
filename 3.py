import sys

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
        if len(s) == 0:
            return 0
        str_len = len(s)
        max_len = 1
        begin = 0
        last_pos = {s[0]: 0}
        for i in xrange(1, str_len):
            if s[i] in last_pos and last_pos[s[i]] >= begin:
                begin = last_pos[s[i]] + 1
            else:
                max_len = max(max_len, i - begin + 1)
            last_pos[s[i]] = i
        return max_len
        
if __name__ == '__main__':
    sol = Solution()
    print sol.lengthOfLongestSubstring(sys.argv[1])
