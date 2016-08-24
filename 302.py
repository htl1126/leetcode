# ref: https://discuss.leetcode.com/topic/29086/clear-binary-search-python


class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        def find(lo, hi, check):
            while lo < hi:
                mid = (lo + hi) / 2
                if check(mid):
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        top = find(0, x, lambda x: '1' in image[x])
        bottom = find(x, len(image), lambda x: '1' not in image[x])
        left = find(0, y, lambda y: any(row[y] == '1' for row in image))
        right = find(y, len(image[0]), lambda y: all(row[y] == '0'
                                                     for row in image))
        return (right - left) * (bottom - top)

if __name__ == '__main__':
    sol = Solution()
    print sol.minArea([list('0010'), list('0110'), list('0100')], 0, 2)
