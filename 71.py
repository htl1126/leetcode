# ref: https://discuss.leetcode.com/topic/28240/9-lines-of-python-code


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        places = [p for p in path.split('/') if p != '' and p != '.']
        stack = []
        for place in places:
            if place == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(place)
        return '/' + '/'.join(stack)

if __name__ == '__main__':
    sol = Solution()
    print sol.simplifyPath('/../')
