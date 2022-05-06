# Ref: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/discuss/360962/JavaPython-3-Count-chars-in-each-word-.

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_cnt = collections.Counter(chars)
        ans = 0
        for word in words:
            w_cnt = collections.Counter(word)
            for w in w_cnt:
                if w_cnt[w] > chars_cnt[w]:
                    break
            else:
                ans += len(word)
        return ans
