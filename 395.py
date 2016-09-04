# ref: https://discuss.leetcode.com/topic/57092/6-lines-python


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))

if __name__ == '__main__':
    sol = Solution()
    cases = [['aaabb', 3]]
    for case in cases:
        print cases
        print sol.longestSubstring(case[0],  case[1])
