# math solution

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Input: s = "PAYPALISHIRING", numRows = 4
        # Output: "PINALSIGYAHRPI"
        # Explanation:
        # P     I    N
        # A   L S  I G
        # Y A   H R
        # P     I
        # ^^^^^
        # Split every (numRows - 1) * 2 chars as groups
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
