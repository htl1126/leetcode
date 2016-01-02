# make use of power of list comprehension to make code concise
# source: https://leetcode.com/discuss/76737/clean-dp-python-code

import sys
from leetcode_util import read_list

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = float('inf')
        table = [0] + [MAX] * amount
        for i in xrange(1, amount + 1):
            table[i] = min(table[i - coin] if i >= coin else MAX for coin in coins) + 1
        return -1 if table[amount] == MAX else table[amount]

if __name__ == '__main__':
    sol = Solution()
    print sol.coinChange(read_list(sys.argv[1]), int(sys.argv[2]))
