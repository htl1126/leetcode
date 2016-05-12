class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_dis = 99999
        pos_1, pos_2 = None, None
        for i in xrange(len(words)):
            if words[i] == word1:
                pos_1 = i
            if words[i] == word2:
                pos_2 = i
            if pos_1 != None and pos_2 != None:
                if abs(pos_1 - pos_2) < min_dis:
                    min_dis = abs(pos_1 - pos_2)
        return min_dis

if __name__ == '__main__':
    sol = Solution()
    print sol.shortestDistance(["practice", "makes", "perfect", "coding",
                                "makes"], 'coding', 'practice')
