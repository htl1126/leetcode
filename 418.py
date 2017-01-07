# ref: https://discuss.leetcode.com/topic/67721/9-lines-in-python


class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ' '.join(sentence) + ' '
        start, l = 0, len(s)
        for i in xrange(rows):
            start += cols
            while s[start % l] != ' ':
                start -= 1
            start += 1
        return start / l

if __name__ == '__main__':
    sol = Solution()
    print sol.wordsTyping(["I", "had", "apple", "pie"], 4, 5)
