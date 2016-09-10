class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        def search(pattern, str, dic):
            if not pattern:
                return str == ''
            if pattern[0] in dic:
                target = dic[pattern[0]]
                if len(str) >= len(target) and str[:len(target)] == target:
                    return search(pattern[1:], str[len(target):], dic)
            else:
                for i in xrange(1, len(str) - len(pattern) + 2):
                    if str[:i] not in dic.values():
                        dic[pattern[0]] = str[:i]
                        if search(pattern[1:], str[i:], dic):
                            return True
                        del dic[pattern[0]]
            return False
        return search(pattern, str, {})

if __name__ == '__main__':
    sol = Solution()
    print sol.wordPatternMatch('aabb', 'xyzabcxzyabc')
