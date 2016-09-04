class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, i, n = [[1, '']], 0, len(s)
        while i < n:
            c = s[i]
            if 'a' <= c <= 'z':
                stack[-1][1] += c
            elif '0' <= c <= '9':
                j = i
                while '0' <= s[j] <= '9':
                    j += 1
                stack += [int(s[i:j]), ''],
                i = j
            elif c == ']':
                j, t = stack.pop()
                stack[-1][1] += t * j
            else:
                stack[-1][1] += c
            i += 1
        return stack[0][1]

if __name__ == '__main__':
    sol = Solution()
    testcase = ['3[a]2[bc]', '3[a2[c]]', '2[abc]3[cd]ef']
    for i, case in enumerate(testcase):
        print i, case
        print sol.decodeString(case)
