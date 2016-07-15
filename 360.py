# ref: https://discuss.leetcode.com/topic/48436/simple-and-concise-o
#              -n-solution/14


class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        f_vals = map(lambda x: a * x ** 2 + b * x + c, nums)
        offset = c - b * b / a / 4.0 if a != 0 else 0
        ans = []
        l, r = 0, len(nums) - 1
        while l <= r:
            if offset != 0:
                diff = abs(f_vals[l] - offset) - abs(f_vals[r] - offset)
            else:
                diff = f_vals[l] - f_vals[r]
            if diff >= 0:
                ans.append(f_vals[l])
                l += 1
            else:
                ans.append(f_vals[r])
                r -= 1
        return ans if ans[0] < ans[-1] else ans[::-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.sortTransformedArray([-4, -2, 2, 4], 0, 3, 5)
