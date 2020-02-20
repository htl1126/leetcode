class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return -1
        digits = list(str(n))
        size = len(digits)
        for i in xrange(size - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                min_idx = i + 1
                for j in xrange(i + 2, size):
                    if digits[j] < digits[min_idx] and digits[j] > digits[i]:
                        min_idx = j
                digits[i], digits[min_idx] = digits[min_idx], digits[i]
                res = int("".join(digits[:i + 1] + sorted(digits[i + 1:])))
                return res if res <= ((1 << 31) - 1) else -1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print sol.nextGreaterElement(12)
