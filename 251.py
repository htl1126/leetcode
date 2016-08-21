# ref: https://discuss.leetcode.com/topic/20896/my-python-solution


class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.x, self.y, self.vec = 0, 0, vec2d

    def next(self):
        """
        :rtype: int
        """
        ans = self.vec[self.x][self.y]
        self.y += 1
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.x < len(self.vec):
            if self.y < len(self.vec[self.x]):
                return True
            self.x += 1
            self.y = 0
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

if __name__ == '__main__':
    i, v = Vector2D([[1, 2], [3], [], [4, 5, 6], []]), []
    while i.hasNext():
        v.append(i.next())
    print v
