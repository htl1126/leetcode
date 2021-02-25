# Ref: https://leetcode.com/problems/design-in-memory-file-system/discuss/103359/Python-Straightforward-with-Explanation

import collections

Trie = lambda: collections.defaultdict(Trie)

class FileSystem:

    def __init__(self):
        self.fs = Trie()
        self.fileinfo = collections.defaultdict(str)

    def ls(self, path: str):
        if path in self.fileinfo:
            return path.split('/')[-1:]

        cur = self.fs
        for token in path.split('/'):
            if token in cur:
                cur = cur[token]
            elif token:
                return []
        return sorted(cur.keys())       

    def mkdir(self, path: str) -> None:
        cur = self.fs
        for token in path.split('/'):
            cur = cur[token]

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)
        self.fileinfo[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.fileinfo[filePath]

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
