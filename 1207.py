class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        occurs = count.values()
        return len(occurs) == len(set(occurs))
