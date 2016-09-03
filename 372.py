# ref: https://discuss.leetcode.com/topic/50591/fermat-and-chinese-remainder


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        def mod(p):
            return pow(a, reduce(
                lambda e, d: (10*e + d) % (p-1), b, 0), p) if a % p else 0
        return (764 * mod(7) + 574 * mod(191)) % 1337

if __name__ == '__main__':
    sol = Solution()
    print sol.superPow(2, [1, 0])
