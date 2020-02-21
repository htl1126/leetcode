# Ref: https://leetcode.com/problems/next-greater-element-i/discuss/515153/Python-monotonic-stack
# Algo: stack

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack, d = [], {}
        for i in nums2:
            while stack and stack[-1] < i:
                d[stack.pop()] = i
            stack.append(i)
        return [d.get(i, -1) for i in nums1]

if __name__ == "__main__":
    sol = Solution()
    print sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
