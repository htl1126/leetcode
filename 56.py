# ref: https://leetcode.com/discuss/42344/7-lines-easy-python


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if result and result[-1][1] >= i[0]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result.append(i)
        return result

if __name__ == '__main__':
    sol = Solution()
    print sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
