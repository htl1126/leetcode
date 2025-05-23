# ref: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/solutions/6659008/beats-2-approach-super-easy-beginners-java-js-c-c-python-dart

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = {}

        for i, num in enumerate(nums):
            if num in d:
                d[num].append(i)
            else:
                d[num] = [i]

        ans = 0
        for num in d:
            indexes = d[num]
            for i in range(len(indexes) - 1):
                for j in range(i + 1, len(indexes)):
                    if indexes[i] * indexes[j] % k == 0:
                        ans += 1

        return ans

