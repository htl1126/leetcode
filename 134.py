# ref: https://discuss.leetcode.com/topic/27760/possibly-the-most-easiest
#              -approach-o-n-one-variable-python


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost or sum(gas) < sum(cost):
            return -1
        balance, begin = 0, 0
        for i in xrange(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                balance = 0
                begin = i + 1
        return begin
