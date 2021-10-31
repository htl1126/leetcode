class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = collections.Counter(arr)
        i = 0
        for w in arr:
            if d[w] == 1:
                i += 1
            if i == k:
                return w
            """
            The loop body is faster than
            if d[w] == 1:
                i += 1
                if i == k:
                    return w
            """
        return ""
