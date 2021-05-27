# Ref: https://leetcode.com/problems/utf-8-validation/discuss/87494/Short'n'Clean-12-lines-Python-solution

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(nums, start, size):
            for i in range(start + 1, start + size + 1):
                if i >= len(nums) or nums[i] >> 6 != 1 << 1:
                    return False
            return True
        i = 0
        while i < len(data):
            first = data[i]
            if first >> 7 == 0:
                i += 1
            elif first >> 5 == (1 << 3) - 2 and check(data, i, 1):
                i += 2
            elif first >> 4 == (1 << 4) - 2 and check(data, i, 2):
                i += 3
            elif first >> 3 == (1 << 5) - 2 and check(data, i, 3):
                i += 4
            else:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    testcase = [[197, 130, 1], [235, 140, 4], [145]]
    for i in xrange(3):
        print i, testcase[i]
        print sol.validUtf8(testcase[i])
