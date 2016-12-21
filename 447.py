# ref: https://discuss.leetcode.com/topic/66813/short-python-o-n-2-hashmap
#              -solution

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
          cmap = {}
          for q in points:
              dx, dy = p[0] - q[0], p[1] - q[1]
              cmap[dx * dx + dy * dy] = 1 + cmap.get(dx * dx + dy * dy, 0)
          for k in cmap:
              res += cmap[k] * (cmap[k] - 1)
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]])
