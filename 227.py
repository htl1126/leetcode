# ref: https://discuss.leetcode.com/topic/16807/17-lines-c-easy-20-ms
import re


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = ''.join(s.split())
        item_lst = re.split('(\D)', s)
        item_lst = ['+'] + [int(item_lst[i]) if i % 2 == 0 else item_lst[i]
                            for i in xrange(len(item_lst))] + ['+']
        i, item_len, total, term, n = 0, len(item_lst), 0, 0, 0
        while i < item_len:
            if item_lst[i] in '+-':
                total += term
                if i + 1 >= item_len:
                    break
                term = [-1, 1][item_lst[i] == '+'] * item_lst[i + 1]
                i += 2
            else:
                n = item_lst[i + 1]
                if item_lst[i] == '*':
                    term *= n
                else:
                    term = term / n if term > 0 else - (- term / n)  # case -3/2
                i += 2
        return total

if __name__ == '__main__':
    sol = Solution()
    print sol.calculate('14-3/2')
