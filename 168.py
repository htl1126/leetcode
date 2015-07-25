# Solution Key: Convert a decimal number to a number of base 26
class Solution:
    # @return a string
    def convertToTitle(self, num):
        result = ""
        num -= 1
        while True:
            if num < 0:
                break
            current_digit = num % 26
            num = num / 26 - 1
            current_alphabet = chr(ord('A') + current_digit)
            result = "{0}{1}".format(result, current_alphabet)
        result = result[::-1]
        return result
