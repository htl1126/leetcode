# Ref: https://leetcode.com/problems/find-duplicate-file-in-system/discuss/104122/Python-Straightforward-with-Explanation

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for line in paths:
            item = line.split()
            path = item[0]
            for file in item[1:]:
                fname, name = file.split('(')
                d[name[:-1]].append(path + '/' + fname)
        return [d[l] for l in d if len(d[l]) > 1]
