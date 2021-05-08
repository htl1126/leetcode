# Ref: https://leetcode.com/problems/top-k-frequent-words/discuss/108348/Python-3-solution-with-O(nlogk)-and-O(n)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        heap = []
        for w, f in count.items():
            heapq.heappush(heap, Word(w, f))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap).word)
        return ans[::-1]


# We have a different ways of sorting words with the same frequency. So we have this class.
class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq: # notice here
            return self.word > other.word
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word
