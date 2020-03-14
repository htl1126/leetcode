class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digit = list(str(num))
        for i in xrange(len(digit)):
            if digit[i] != '9':
                max_digit = i + 1
                for j in xrange(i + 1, len(digit)):
                    if digit[j] >= digit[max_digit]:
                        max_digit = j
                if 0 <= i < len(digit) and 0 <= max_digit < len(digit) and digit[max_digit] > digit[i]:
                    digit[i], digit[max_digit] = digit[max_digit], digit[i]
                    break
        return int(''.join(digit))

if __name__ == "__main__":
    sol = Solution()
    print sol.maximumSwap(1000)
