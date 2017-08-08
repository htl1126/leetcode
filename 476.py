class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 1
        ans, power_two = 0, 1
        while num:
            ans += (1 - num % 2) * power_two
            power_two <<= 1
            num >>= 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.findComplement(4)
