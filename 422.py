# ref: https://discuss.leetcode.com/topic/63423/1-liner-python


class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        return map(None, *words) == map(None, *map(None, *words))
