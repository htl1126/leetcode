# Ref: https://leetcode.com/problems/string-compression/discuss/92568/Python-Two-Pointers-O(n)-time-O(1)-space

class Solution:
    def compress(self, chars: List[str]) -> int:
        res = i = 0
        size = len(chars)
        while i < size:
            c, length = chars[i], 1
            while (i + 1) < size and c == chars[i + 1]:
                i, length = i + 1, length + 1
            chars[res] = c
            if length > 1:
                len_str = str(length)
                chars[res + 1:res + 1 + len(len_str)] = len_str
                res += len(len_str)
            res, i = res + 1, i + 1
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.compress(["a","a","a","b","b","a","a"])
