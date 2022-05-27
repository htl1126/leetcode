# Ref: https://leetcode.com/problems/synonymous-sentences/discuss/430534/Python-bfs-solution

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        g = collections.defaultdict(dict)
        q = collections.deque()
        ans = set()
        q.append(text)
        for s in synonyms:
            g[s[0]][s[1]] = 1
            g[s[1]][s[0]] = 1
        while q:
            s = q.popleft()
            ans.add(s)
            w_list = s.split()
            for i, w in enumerate(w_list):
                if w in g:
                    for w2 in g[w]:
                        new_s = ' '.join(w_list[:i] + [w2] + w_list[i + 1:])
                        if new_s not in ans:
                            q.append(new_s)
        return sorted(list(ans))
