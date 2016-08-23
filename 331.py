# ref: https://discuss.leetcode.com/topic/36034/6-lines-python-7-lines-java
# The number of null nodes is one larger than non-left nodes


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        need = 1
        for val in preorder.split(','):
            if not need:
                return False
            need -= ' #'.find(val)
        return not need

if __name__ == '__main__':
    sol = Solution()
    print sol.isValidSerialization('9,3,4,#,#,1,#,#,2,#,6,#,#')
