# ref: https://discuss.leetcode.com/topic/20750/3-lines-ruby-5-lines-python


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        nums = n % 2 * list('018') or ['']
        while n > 1:
            n -= 2
            nums = [a + num + b for a, b in '00 11 88 96 69'.split()[n < 2:]
                    for num in nums]
        return nums

if __name__ == '__main__':
    sol = Solution()
    print sol.findStrobogrammatic(3)
