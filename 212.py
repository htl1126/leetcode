# ref: https://discuss.leetcode.com/topic/14307/27-lines-uses-complex-numbers


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[None] = True
        board = {(i, j): c
                 for i, row in enumerate(board)
                 for j, c in enumerate(row)}
        found = []

        def search(node, i, j, word):
            if node.pop(None, None):
                found.append(word)
            c = board.get((i, j))
            if c in node:
                board[(i, j)] = None
                for x, y in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
                    search(node[c], x, y, word + c)
                board[(i, j)] = c
        for i, j in board:
            search(root, i, j, '')

        return found

if __name__ == '__main__':
    sol = Solution()
    board = [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']]
    words = ['oath', 'pea', 'eat', 'rain']
    print sol.findWords(board, words)
