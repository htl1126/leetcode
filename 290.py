class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_pool = str.split(' ')
        str_seen = []
        str_dict = {}
        if len(pattern) != len(str_pool):
            return False
        for i in xrange(len(pattern)):
            if pattern[i] in str_dict and str_dict[pattern[i]] != str_pool[i]:
                return False
            elif pattern[i] not in str_dict and str_pool[i] in str_seen:
                return False
            else:
                str_dict[pattern[i]] = str_pool[i]
                str_seen.append(str_pool[i])
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.wordPattern('abba', 'ab ab ab ab')
