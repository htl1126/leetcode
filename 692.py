import collections
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        class FreqWord(object):
            def __init__(self, freq, word):
                self.freq = freq
                self.word = word
            def __eq__(self, other):
                return self.freq == other.freq and self.word == other.word
            def __lt__(self, other):
                return self.freq < other.freq or (self.freq == other.freq and self.word > other.word)

        d = collections.Counter(words)
        pq = [FreqWord(-float('inf'), '') for _ in xrange(k)]
        for word, count in d.items():
            heapq.heappushpop(pq, FreqWord(count, word))

        ans = []
        for _ in xrange(k):
            ans.append(heapq.heappop(pq).word)

        return ans[::-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
