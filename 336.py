# ref: https://discuss.leetcode.com/topic/39526/python-solution


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        d, res = dict([(w[::-1], i) for i, w in enumerate(words)]), []
        for i, w in enumerate(words):
            for j in xrange(len(w) + 1):
                prefix, postfix = w[:j], w[j:]
                # prefix + postfix + prefix[::-1] is a palindrome
                if prefix in d and i != d[prefix] and postfix == postfix[::-1]:
                    res.append([i, d[prefix]])
                # postfix[::-1] + prefix + postfix is a palindrome, 'j > 0'
                # prevents empty prefix
                if j > 0 and postfix in d and i != d[postfix] and \
                        prefix == prefix[::-1]:
                    res.append([d[postfix], i])
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
