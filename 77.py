# ref: https://discuss.leetcode.com/topic/14626/1-liner-3-liner-4-liner


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]

        ans = []
        for i in range(k, n + 1):
            for pre in self.combine(i - 1, k - 1):
                ans.append(pre + [i])
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.combine(4, 2)
