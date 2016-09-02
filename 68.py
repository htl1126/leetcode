# ref: https://discuss.leetcode.com/topic/25970/concise-python-solution-10-lines


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, cur, num_letter = [], [], 0
        for w in words:
            if num_letter + len(cur) + len(w) > maxWidth:
                if len(cur) == 1:
                    cur[0] += ' ' * (maxWidth - num_letter)
                else:
                    nBin, minBinSize = len(cur) - 1, (maxWidth - num_letter) / \
                        (len(cur) - 1)
                    for i in xrange(nBin):
                        cur[i] += ' ' * minBinSize
                        if i < (maxWidth - num_letter) % nBin:
                            cur[i] += ' '
                res.append(''.join(cur))
                cur, num_letter = [], 0
            cur += [w]
            num_letter += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]

if __name__ == '__main__':
    sol = Solution()
    print sol.fullJustify(["This", "is", "an", "example", "of", "text",
                           "justification."], 16)
