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
            t = []
            if n >= 2:
                for num in nums:
                    for a, b in ['00', '11', '88', '96', '69']:
                        t.append(a + num + b)
            else:
                for num in nums:
                    for a, b in ['11', '88', '96', '69']:
                        t.append(a + num + b)
            nums = t
        return nums

if __name__ == '__main__':
    sol = Solution()
    print sol.findStrobogrammatic(3)
