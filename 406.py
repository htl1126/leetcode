# ref: https://discuss.leetcode.com/topic/60394/easy-concept-with-python-ac
#              -solution


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for p in sorted(people, key=lambda x: (-x[0], x[1])):
            res.insert(p[1], p)
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
