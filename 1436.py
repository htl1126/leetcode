# Ref: https://leetcode.com/problems/destination-city/discuss/621261/Python-1-Set.-Faster-than-98

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source_list = set(p[0] for p in paths)
        for p in paths:
            if p[1] not in source_list:
                return p[1]
