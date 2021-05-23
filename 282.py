# ref: https://discuss.leetcode.com/topic/30089/clean-python-dfs-with-comments


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        def dfs(num, temp, cur, last, res):
            if not num:
                if cur == target:
                    res.append(temp)
                return
            for i in range(1, len(num) + 1):
                val = num[:i]
                if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
                    dfs(num[i:], temp + "+" + val, cur + int(val), int(val), res)
                    dfs(num[i:], temp + "-" + val, cur - int(val), - int(val), res)
                    dfs(num[i:], temp + "*" + val, cur - last + last * int(val), last*int(val), res)
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
                dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.addOperators('105', 5)
