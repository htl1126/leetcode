class Solution:
    def minDistance(self, height: int, width: int, tree, squirrel, nuts) -> int:
        dis_sum = sum(2 * (abs(i - tree[0]) + abs(j - tree[1])) for i, j in nuts)
        return min(dis_sum - (abs(i - tree[0]) + abs(j - tree[1])) + (abs(i - squirrel[0]) + abs(j - squirrel[1])) for i, j in nuts)

if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance(5, 7, [2, 2], [4, 4], [[3, 0], [2, 5]]))
