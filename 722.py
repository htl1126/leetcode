class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        in_comment_block = False
        comment_block_start = (None, None)
        ans = []
        cur = ""
        for j in xrange(len(source)):
            s = source[j]
            s_len = len(s)
            for i, c in enumerate(s):
                if not in_comment_block:
                    if c == '/':
                        if i + 1 < s_len and s[i + 1] == '/':
                            break
                        elif i + 1 < s_len and s[i + 1] == '*':
                            in_comment_block = True
                            comment_block_start = (j, i + 1)
                            continue
                    cur += c
                else:
                    if c == '/' and i - 1 >= 0 and s[i - 1] == '*' and (j, i - 1) != comment_block_start:
                        in_comment_block = False
                        comment_block_start = (None, None)
            if cur != "" and not in_comment_block:
                ans.append(cur)
                cur = ""
        return ans

if __name__ == "__main__":
    sol = Solution()
    source = ["a/*/b//*c","blank","d/*/e*//f"]
    print sol.removeComments(source)