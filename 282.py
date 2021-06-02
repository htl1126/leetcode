# ref: https://discuss.leetcode.com/topic/30089/clean-python-dfs-with-comments


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        def dfs(rest_s, cur_s, cur_sum, last_term):
            if not rest_s:
                if cur_sum == target:
                    res.append(cur_s)
                return
            for i in range(1, len(rest_s) + 1):
                val = rest_s[:i]
                if i == 1 or (i > 1 and rest_s[0] != "0"):  # prevent "00*" as a number
                    dfs(rest_s[i:], cur_s + "+" + val, cur_sum + int(val), int(val))
                    dfs(rest_s[i:], cur_s + "-" + val, cur_sum - int(val), - int(val))
                    dfs(rest_s[i:], cur_s + "*" + val, cur_sum - last_term + last_term * int(val), last_term * int(val))
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
                dfs(num[i:], num[:i], int(num[:i]), int(num[:i]))
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.addOperators('105', 5)
