# ref: https://discuss.leetcode.com/topic/60394/easy-concept-with-python-ac
#              -solution
import itertools


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for k, g in itertools.groupby(sorted(people, reverse=True),
                                      key=lambda x: x[0]):
            for person in sorted(g):
                res.insert(person[1], person)
        return res
