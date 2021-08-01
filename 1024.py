# ref: https://leetcode.com/problems/video-stitching/discuss/270036/JavaC%2B%2BPython-Greedy-Solution-O(1)-Space

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        ans, start, end = 0, -1, 0
        for i, j in sorted(clips):
            if end >= time or i > end:
                break
            elif start < i <= end:
                ans, start = ans + 1, end
            end = max(end, j)
        return ans if end >= time else -1
