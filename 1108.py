class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = []
        for c in address:
            if c == '.':
                ans.append("[.]")
            else:
                ans.append(c)
        return "".join(ans)
