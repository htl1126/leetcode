# Ref: https://leetcode.com/problems/campus-bikes/discuss/341433/Python-simple-and-fast-solution
# Algo: greedy

class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        distances = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distances.append((distance, i, j))
        distances.sort()
        num_worker = len(workers)
        ans = [-1 for _ in xrange(num_worker)]
        bike_taken = set()
        for distance, i, j in distances:
            if ans[i] == -1 and j not in bike_taken:
                ans[i] = j
                bike_taken.add(j)
            if len(bike_taken) == num_worker:
                break
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.assignBikes([[0, 0], [2, 1]], [[1, 2], [3, 3]])
