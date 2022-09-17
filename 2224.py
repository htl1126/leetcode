class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        diff = int(correct[:2]) * 60 + int(correct[3:]) - int(current[:2]) * 60 - int(current[3:])
        ans = 0
        for n in [60, 15, 5, 1]:
            ans += diff // n
            diff -= diff // n * n
        return ans
