class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        for i in xrange(len(digits) - 1, 0, -1):
            if digits[i] >= 10:
                digits[i] -= 10
                digits[i - 1] += 1
        return digits if digits[0] < 10 else [1] + [digits[0] - 10] + digits[1:]
