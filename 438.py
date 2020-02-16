# Ref: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92009/Python-Sliding-Window-Solution-using-Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        i, p_len, s_len = 0, len(p), len(s)
        cnt_p, cnt_s = Counter(p), Counter(s[:p_len - 1])
        ans = []
        while i + p_len <= s_len:
            cnt_s[s[i + p_len - 1]] += 1
            if cnt_s == cnt_p:
                ans.append(i)
            cnt_s[s[i]] -= 1
            if cnt_s[s[i]] == 0:
                del cnt_s[s[i]]
            i += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.findAnagrams("cbaebabacd", "abc")
