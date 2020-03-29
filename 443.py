class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        seg_start, ans = 0, 0
        for i in xrange(len(chars)):
            if chars[seg_start] != chars[i]:
                seg_len = i - seg_start
                chars[ans] = chars[seg_start]
                if seg_len > 1:
                    chars[ans + 1:ans + len(str(seg_len)) + 1] = list(str(seg_len))
                ans += 1 + (len(str(seg_len)) if seg_len > 1 else 0)
                seg_start = i
        seg_len = len(chars) - seg_start
        chars[ans] = chars[seg_start]
        if seg_len > 1:
            chars[ans + 1:ans + len(str(seg_len)) + 1] = list(str(seg_len))
        ans += 1 + (len(str(seg_len)) if seg_len > 1 else 0)
        chars = chars[:ans]
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.compress(["a","a","a","b","b","a","a"])
