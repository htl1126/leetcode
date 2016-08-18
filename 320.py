class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        w_len = len(word)
        res = []
        for i in xrange(2 ** w_len):
            num = i
            abbr = ''
            abbr_num = 0
            for j in xrange(w_len - 1, -1, -1):
                if num & 1:
                    if abbr_num:
                        abbr += str(abbr_num)[::-1]
                        abbr_num = 0
                    abbr += word[j]
                else:
                    abbr_num += 1
                num >>= 1
            if abbr_num:
                abbr += str(abbr_num)[::-1]
            res += [abbr[::-1]]
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.generateAbbreviations('dictionary')
