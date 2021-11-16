class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols, ans = len(encodedText) // rows, []
        for c in range(cols):
            for i in range(rows):
                if c + i < cols:
                    ans.append(encodedText[i * cols + c + i])
                else:
                    break
        return ''.join(ans).rstrip()
