class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        table = [1]
        for i in range(1, 32):
            table.append(table[-1] * 2)
        table = ["".join(sorted(str(i))) for i in table]
        print(table)
        S = "".join(sorted(str(N)))
        for val in table:
            if S == val:
                return True
        return False
