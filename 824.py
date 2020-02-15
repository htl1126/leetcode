class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split(' ')
        for i in xrange(len(words)):
            s = words[i]
            if s[0] in "aeiouAEIOU":
                s += "ma"
            else:
                s = s[1:] + s[0] + "ma"
            s += 'a' * (i + 1)
            words[i] = s
        return ' '.join(words)

if __name__ == "__main__":
    sol = Solution()
    print sol.toGoatLatin("The quick brown fox jumped over the lazy dog")
