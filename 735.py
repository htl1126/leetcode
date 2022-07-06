# Ref: https://leetcode.com/problems/asteroid-collision/discuss/109666/Python-O(n)-Stack-based-with-explanation

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for asteroid in asteroids:
            while len(ans) and asteroid < 0 and ans[-1] > 0:
                if ans[-1] == -asteroid:
                    ans.pop()
                    break
                if ans[-1] < -asteroid:
                    ans.pop()
                    continue
                if ans[-1] > -asteroid:
                    break
            else:
                ans.append(asteroid)
        return ans
