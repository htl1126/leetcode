# ref: https://discuss.leetcode.com/topic/55097/simple-python-solution


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen, pathlen = 0, {0: 0}
        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen

if __name__ == '__main__':
    sol = Solution()
    print sol.lengthLongestPath('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1'
                                '\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext')
