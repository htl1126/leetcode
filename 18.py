# ref: https://leetcode.com/discuss/28936/a-conise-python-solution-based-on-ksum


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        num = sorted(nums)

        def ksum(num, k, target):
            i = 0
            result = set()
            if target < sum(num[:k]) or len(num) < k:
                return result
            if k == 2:
                j = len(num) - 1
                while i < j:
                    if num[i] + num[j] == target:
                        result.add((num[i], num[j]))
                        i += 1
                    elif num[i] + num[j] > target:
                        j -= 1
                    else:
                        i += 1
            else:
                while i < len(num) - k + 1:
                    new_target = target - num[i]
                    subresult = ksum(num[i + 1:], k - 1, new_target)
                    if subresult:
                        result = result | set((num[i],) + tuple
                                              for tuple in subresult)
                    i += 1
            return result
        return [list(tuple) for tuple in ksum(num, 4, target)]

if __name__ == '__main__':
    sol = Solution()
    print sol.fourSum([0], 0)
