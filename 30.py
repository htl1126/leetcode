# ref: https://discuss.leetcode.com/topic/10665/concise-python-code-using
#              -defaultdict
import collections
import copy


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not words[0]:
            return None
        wl, total, strlen, res = (len(words[0]), len(words) * len(words[0]),
                                  len(s), [])
        word_ctr = collections.Counter(words)
        for i in xrange(wl):
            j = i
            count = copy.copy(word_ctr)
            while j < strlen - wl + 1:
                count[s[j:j + wl]] -= 1
                while count[s[j:j + wl]] < 0:
                    count[s[i:i + wl]] += 1
                    i += wl
                j += wl
                if j - i == total:
                    res += i,
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.findSubstring('barfoothefoobarman', ['foo', 'bar'])
