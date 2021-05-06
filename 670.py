class Solution:
    def maximumSwap(self, num: int) -> int:
        n = [int(i) for i in str(num)]
        dic = {x: i for i, x in enumerate(n)}
        for i, d in enumerate(n):
            for D in range(9, d, -1):
                if dic.get(D, -1) > i:
                    n[i], n[dic[D]] = n[dic[D]], n[i]
                    return int(''.join(str(i) for i in n))
        return num

if __name__ == "__main__":
    sol = Solution()
    print sol.maximumSwap(1000)
