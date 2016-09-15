# ref: https://discuss.leetcode.com/topic/32108/python-solutions


class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        return [word] + [word[:first] + str(last - first + 1) +
                         word[last + 1:last + 2] + rest
                         for last in xrange(len(word))
                         for first in xrange(last + 1)
                         for rest
                         in self.generateAbbreviations(word[last + 2:])]

if __name__ == '__main__':
    sol = Solution()
    print sol.generateAbbreviations('dictionary')
