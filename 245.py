# ref: https://leetcode.com/discuss/50715/12-16-lines-java-c


class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1, i2 = 9999999, -9999999
        dist = 9999999
        for i in xrange(len(words)):
            if words[i] == word1:
                if word1 == word2:
                    i1 = i2
                    i2 = i
                else:
                    i1 = i
            elif words[i] == word2:
                i2 = i
            dist = min(dist, abs(i1 - i2))
        return dist

if __name__ == '__main__':
    sol = Solution()
    print sol.shortestWordDistance([
        "practice", "makes", "perfect", "coding", "makes"], 'makes', 'makes')
