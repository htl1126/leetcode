# math solution

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) == 0:
            return s
        result = [''] * numRows
        num = (numRows - 1) * 2
        for i, item in enumerate(s):
            if i % num >= numRows:
                result[num - i % num] += item
            else:
                result[i % num] += item
        return ''.join(result)
        
if __name__ == '__main__':
    sol = Solution()
    print sol.convert('PAYPALISHIRING', 3)
