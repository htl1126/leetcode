# ref: https://discuss.leetcode.com/topic/14307/27-lines-uses-complex-numbers


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[None] = True
        board = {i + 1j*j: c
                 for i, row in enumerate(board)
                 for j, c in enumerate(row)}
        found = []

        def search(node, z, word):
            if node.pop(None, None):
                found.append(word)
            c = board.get(z)
            if c in node:
                board[z] = None
                for k in xrange(4):
                    search(node[c], z + 1j**k, word + c)
                board[z] = c
        for z in board:
            search(root, z, '')

        return found

if __name__ == '__main__':
    sol = Solution()
    board = [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']]
    words = ['oath', 'pea', 'eat', 'rain']
    print sol.findWords(board, words)
