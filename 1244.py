# Ref: https://leetcode.com/problems/design-a-leaderboard/discuss/418866/Python-Counter-1-line-Each
class Leaderboard:

    def __init__(self):
        self.scores = collections.Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        return sum(v for k, v in self.scores.most_common(K))

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

