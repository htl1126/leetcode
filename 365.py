# ref: https://discuss.leetcode.com/topic/49262/a-little-explanation-on-gcd
#              -method-c-java-python


class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def get_gcd(a, b):
            return get_gcd(b, a % b) if b else a
        gcd = get_gcd(x, y)
        return z % gcd == 0 and x + y >= z if gcd else z == 0

if __name__ == '__main__':
    sol = Solution()
    print sol.canMeasureWater(0, 5, 0)
