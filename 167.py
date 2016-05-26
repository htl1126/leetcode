# ref: https://leetcode.com/discuss/52728/python-different-solutions-
#              pointer-dictionary-binary-search


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for idx, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, idx + 1]
            dic[num] = idx

if __name__ == '__main__':
    sol = Solution()
    print sol.twoSum([0, 0, 1, 2], 0)
