# ref: https://leetcode.com/discuss/64749/my-python
#      -solution-with-o-n-time-and-o-1-space
# keep track of last occurrence for each alphabet
# update longest sequence length when facing a new alphabet


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        begin, ans = 0, 0
        for i, c in enumerate(s):
            if c in dic and dic[c] >= begin:  # notice "dic[c] >= begin", case: "abba"
                begin = dic[c] + 1
            ans = max(ans, i - begin + 1)
            dic[c] = i
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.lengthOfLongestSubstring('pwwkew')
