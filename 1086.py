import heapq

class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        scores = {}
        for sid, score in items:
            if sid in scores:
                if len(scores[sid]) == 5:
                    if score > scores[sid][0]:
                        heapq.heapreplace(scores[sid], score)
                else:
                    heapq.heappush(scores[sid], score)
            else:
                scores[sid] = [score]
        ans = []
        for sid in scores:
            ans.append([sid, sum(scores[sid]) / 5])
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.highFive([[2,75],[2,14],[2,35],[2,37],[2,17],[2,0],[2,84],[2,89],[2,11],[2,93],[2,53],[2,14],[2,96],[2,18],[2,20],[2,99],[2,47],[2,9],[2,41],[2,40]])
